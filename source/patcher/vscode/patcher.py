"""google.google-antigravity VS Code 扩展的 Patch / 还原实现。

补丁分两部分：PART 1 在版本检查日志之后注入“已存在二进制则跳过下载”的
守卫；PART 2 将渠道变更判断改为常量 false。同时兼容旧版（未压缩）与
VS Code 1.12.0 的压缩构建。
"""

import os
import re
import shutil
import filecmp

from patcher.constants import COLOR_CYAN, COLOR_GREEN, COLOR_YELLOW
from patcher.utils.console import (
    color,
    info,
    hint,
    ok,
    warn,
    err,
    step,
    print_panel,
)
from patcher.utils.file import (
    file_hash,
    file_size,
    format_bytes,
    fix_posix_permissions,
)
from patcher.utils.update import handle_patch_failure

BAK_EXT = ".vscodebak"


class _ManagerGateAdapter:
    """把 manager 的单匹配接口适配为 agy 的 resolve_all 接口。"""

    def resolve_all(self, data):
        # 延迟导入，避免仅处理 extension.js 时加载二进制 manager 模块。
        from patcher.manager.patcher import MANAGER_GATE

        kind, offset, gate = MANAGER_GATE.resolve(data)
        return [(kind, [offset], gate)]


# VS Code 的 agy --hub 登录还会检查 hasValidAuth；必须与资格页面 gate
# 在同一次写入中处理，否则 OAuth 成功后仍会得到 failure_kind=ineligible。
VSCODE_AGY_EXTRA_GATES = [
    (_ManagerGateAdapter(), "hasValidAuth=true"),
]


# ---------------------------------------------------------------------------
# PART 1 —— extension.js 中的锚点标记与原始语句
PART1_ANCHOR = "outputChannel.appendLine('[INSTALL] Checking Antigravity releases...');"

# PART 1 的宽松 regex：允许不同的引号和空白，但要求匹配完整的
# appendLine 调用（含右括号和可选的 ';'）。
# 这样可保证插入点在调用之后，而不是落在调用内部。
# 第 1 组为整个调用（插入点 = m.end(1)）。
PART1_ANCHOR_RE = re.compile(
    r"(outputChannel\s*\.\s*appendLine\s*\(\s*"            # outputChannel.appendLine(
    r"(['\"])\[INSTALL\]\s*Checking Antigravity releases[^'\"]*\2"  # '锚点字符串'
    r"\s*\)\s*;?)"                                         # ) 或 );
)

# 注入内容：若二进制已下载（targetPathOverride 或 ~/.gemini/bin），
# 则跳过版本检查与重复下载。
PART1_INJECT = (
    "{const __primary=options.targetPathOverride||getInstalledTargetPath();"
    "const __candidates=[__primary,"
    "(0,path_1.join)((0,path_1.dirname)(__primary),'antigravity'+((0,path_1.extname)(__primary)||''))];"
    "for(const __p of __candidates){if(__p&&await pathExists(__p)){"
    "outputChannel.appendLine('[INSTALL] Existing binary found at '+__p+'. "
    "Skipping version check and re-download.');return __p;}}}"
)

# 压缩构建（例如 1.12.0）中 outputChannel/options 等名称被替换成短标识符。
# 因此插入点按稳定的日志文本定位，并绕开压缩后的变量直接计算路径。
PART1_MINIFIED_ANCHOR_RE = re.compile(
    r"((?:[A-Za-z_$][\w$]*\s*\.\s*)?appendLine\s*\(\s*"
    r"(['\"])\[INSTALL\]\s*Checking Antigravity releases[^'\"]*\2"
    r"\s*\)\s*;?)"
)
# 新构建中的 acquireInstalledBinaryPath 期望 action 返回含 installPath 的
# 对象，而不是旧版扩展返回的字符串。
PART1_MINIFIED_INJECT = (
    "{const __fs=require('fs'),__os=require('os'),__path=require('path');"
    "const __ext=process.platform==='win32'?'.exe':'';"
    "for(const __name of['agy','antigravity']){"
    "const __p=__path.join(__os.homedir(),'.gemini','bin',__name+__ext);"
    "if(__fs.existsSync(__p))return{installPath:__p,fellBackToExisting:false};}}"
)

# PART 2 —— 把渠道变更判断替换为常量 false，使扩展不认为渠道发生变化，
# 从而不重新下载二进制。
# 严格 regex：恰好三个标识符（manifestFetched、lastInstalledUrl、
# releaseBaseUrl）且顺序固定 —— 不会误伤 `const X = a && b !== c;`
# 这类无关表达式。
PART2_RE = re.compile(
    r"const\s+isChannelChanged\s*=\s*"
    r"manifestFetched\s*&&\s*lastInstalledUrl\s*!==\s*releaseBaseUrl\s*;"
)
PART2_DONE_RE = re.compile(r"const\s+isChannelChanged\s*=\s*false\s*;")
PART2_REPLACEMENT = "const isChannelChanged = false;"

# 压缩版 1.12.0 用 let <id>=...; 计算 channelChanged，随后立即在带有
# 特征日志的代码块中复用同一个 <id>。反向引用避免误改相邻表达式，
# 日志则用来确认确实命中了目标判断。
PART2_MINIFIED_RE = re.compile(
    r"(?P<decl>\blet\s+(?P<channel>[A-Za-z_$][\w$]*)\s*=\s*)"
    r"(?P<value>[^;]+?)\s*;"
    r"(?=(?P=channel)\s*&&\s*\([\s\S]{0,1600}?"
    r"\[INSTALL\]\s+Release channel change detected)"
)


def is_already_patched(content):
    """当两部分补丁都已应用到 extension.js 时返回 True。"""
    part1_patched = PART1_INJECT in content or PART1_MINIFIED_INJECT in content
    return part1_patched and _apply_part2(content)[1] == "already"


def _apply_part1(content):
    """返回 (新内容, 状态)。状态取值：'applied' | 'already' | 'not-found'。

    不变量：仅当注入代码已存在时返回 'already'，此时内容必须原样返回，
    以保证重复应用补丁是幂等的。
    """
    if PART1_INJECT in content or PART1_MINIFIED_INJECT in content:
        return content, "already"
    m = PART1_ANCHOR_RE.search(content)
    if m:
        insert_at = m.end(1)
        new_content = content[:insert_at] + PART1_INJECT + content[insert_at:]
        return new_content, "applied"
    m = PART1_MINIFIED_ANCHOR_RE.search(content)
    if m:
        insert_at = m.end(1)
        new_content = content[:insert_at] + PART1_MINIFIED_INJECT + content[insert_at:]
        return new_content, "applied"
    # 兜底：按锚点做精确查找（应对特殊格式）
    idx = content.find(PART1_ANCHOR)
    if idx == -1:
        return content, "not-found"
    insert_at = idx + len(PART1_ANCHOR)
    new_content = content[:insert_at] + PART1_INJECT + content[insert_at:]
    return new_content, "applied"


def _apply_part2(content):
    """返回 (新内容, 状态)。状态取值：'applied' | 'already' | 'not-found'。

    先尝试旧版固定写法；压缩版分支只在值尚不为 false 时改写。
    """
    new_content, n = PART2_RE.subn(PART2_REPLACEMENT, content)
    if n:
        return new_content, "applied"

    found_minified = False
    changed_minified = False

    def replace_minified(match):
        nonlocal found_minified, changed_minified
        found_minified = True
        if match.group("value").strip() == "false":
            return match.group(0)
        changed_minified = True
        return match.group("decl") + "false;"

    new_content = PART2_MINIFIED_RE.sub(replace_minified, content)
    if changed_minified:
        return new_content, "applied"
    if found_minified or PART2_DONE_RE.search(content):
        return new_content, "already"
    return content, "not-found"


def _make_backup(path):
    """把 extension.js 备份到 <path>.vscodebak。

    备份与当前文件内容一致时直接复用；扩展已更新（备份过期）时刷新，
    确保写入新补丁之前始终有一份对应的原始文件。
    """
    bak = path + BAK_EXT
    if os.path.exists(bak):
        if filecmp.cmp(path, bak, shallow=False):
            return
        info(f"Backup is stale (extension updated) — refreshing {os.path.basename(path)}{BAK_EXT}")
    else:
        info(f"Creating backup -> {os.path.basename(path)}{BAK_EXT}")
    shutil.copy2(path, bak)
    fix_posix_permissions(bak)
    ok(f"Backup: {os.path.basename(bak)} ({format_bytes(file_size(bak))})")


def do_patch_vscode(extension_js_path):
    """为 google.google-antigravity 扩展的 extension.js 打补丁（PART 1 + PART 2）。

    流程：读取 -> 应用两部分补丁 -> 仅在内容变化时先备份再写入。
    """
    from patcher.cli import confirmed

    if not extension_js_path or not os.path.isfile(extension_js_path):
        err("Antigravity VS Code extension.js not found.")
        hint("Install the 'Google Antigravity' extension in VS Code and run it once.")
        return False

    path = extension_js_path
    info(f"Target: {color(path, COLOR_CYAN)}")
    hint(f"Size: {color(format_bytes(file_size(path)), COLOR_CYAN)}")
    print()

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        err(f"Read error: {e}")
        handle_patch_failure()
        return False

    already = is_already_patched(content)

    new_content, s1 = _apply_part1(content)
    new_content, s2 = _apply_part2(new_content)

    statuses = [s1, s2]
    if all(s == "not-found" for s in statuses):
        err("Patch patterns not found in extension.js (unsupported extension version?).")
        handle_patch_failure()
        return False

    if all(s in ("already", "not-found") for s in statuses) and already:
        hint("extension.js already patched (both parts).")
        if not confirmed("Apply patch anyway?"):
            return True
        # 重新打补丁：若存在备份则先从备份重建，否则直接在现有内容上继续
        bak = path + BAK_EXT
        if os.path.isfile(bak):
            try:
                with open(bak, "r", encoding="utf-8") as f:
                    new_content = f.read()
            except Exception as e:
                warn(f"Could not read backup for re-patch: {e}")
        new_content, s1 = _apply_part1(new_content)
        new_content, s2 = _apply_part2(new_content)

    # 不变量：只有内容确实变化才备份并写入；先备份成功再写，失败时保留原文件
    changed = new_content != content
    if changed:
        try:
            _make_backup(path)
        except (PermissionError, OSError) as e:
            err(f"Backup error: {e}")
            hint("Close VS Code windows and retry. If installed as root, re-run with sudo.")
            handle_patch_failure()
            return False
        try:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(new_content)
        except PermissionError as e:
            err(f"Write error (file locked?): {e}")
            hint("Close VS Code windows and retry.")
            handle_patch_failure()
            return False
        except Exception as e:
            err(f"Write error: {e}")
            handle_patch_failure()
            return False

    applied_parts = sum(1 for s in statuses if s in ("applied", "already"))
    print()
    step("Patch Antigravity VS Code extension", bool(changed or already),
         f"{applied_parts}/2 part(s)")
    print()
    panel_rows = [
        ("Target", os.path.basename(os.path.dirname(path))),
        ("File", os.path.basename(path)),
        ("Part 1", {"applied": "injected skip-download guard",
                    "already": "already patched",
                    "not-found": "pattern not found"}[s1]),
        ("Part 2", {"applied": "isChannelChanged -> false",
                    "already": "already patched",
                    "not-found": "pattern not found"}[s2]),
    ]
    hash_before = file_hash(path)
    panel_rows.append(("Hash", f"{hash_before[:8]}...{hash_before[56:]}" if hash_before else "n/a"))
    print_panel("PATCH COMPLETE" if (changed or already) else "PATCH SKIPPED", panel_rows)
    if changed:
        hint("Reload VS Code window (Developer: Reload Window) for the change to take effect.")
    return True


def do_restore_vscode(extension_js_path):
    """从 .vscodebak 还原 extension.js，并在其曾被 'Antigravity VS Code Patch'
    打过补丁时，从 .agybak 还原 ~/.gemini/bin 下的二进制文件
    （antigravity/agy）。"""
    from patcher.cli import confirmed

    if not extension_js_path or not os.path.isfile(extension_js_path):
        err("Antigravity VS Code extension.js not found.")
        return

    path = extension_js_path
    bak = path + BAK_EXT
    if not os.path.exists(bak):
        warn(f"No backup for {os.path.basename(path)} (nothing to restore).")
        return

    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        err(f"Read error: {e}")
        return

    if not is_already_patched(content):
        warn("extension.js is not patched — skipping restore (backup may be a different build).")
        if not confirmed("Restore from backup anyway?"):
            hint("Restore cancelled.")
            return

    if not confirmed("Restore Antigravity VS Code extension.js from backup?"):
        hint("Restore cancelled.")
        return

    hash_before = file_hash(path)
    try:
        shutil.copy2(bak, path)
        fix_posix_permissions(path)
    except PermissionError as e:
        err(f"Restore error (file locked?): {e}")
        hint("Close VS Code windows and retry.")
        return
    except Exception as e:
        err(f"Restore error: {e}")
        return

    hash_after = file_hash(path)
    print()
    panel_rows = [("Target", os.path.basename(path))]
    if hash_before and hash_after and hash_before != hash_after:
        panel_rows.append(("Before", f"{hash_before[:8]}...{hash_before[56:]}"))
        panel_rows.append(("After", f"{hash_after[:8]}...{hash_after[56:]}"))
    print_panel("RESTORE COMPLETE", panel_rows)
    hint("Reload VS Code window (Developer: Reload Window) for the change to take effect.")

    # --- 还原因 agy 补丁程序而修改过的 ~/.gemini/bin 二进制 ---
    from patcher.vscode.discovery import find_gemini_antigravity_binary
    from patcher.agy.patcher import do_restore_agy

    gemini_bin = find_gemini_antigravity_binary()
    if gemini_bin and os.path.exists(gemini_bin + ".agybak"):
        print()
        info(f"Found patched binary backup: {color(gemini_bin, COLOR_CYAN)}")
        do_restore_agy(gemini_bin)
    elif gemini_bin:
        hint(f"Binary {os.path.basename(gemini_bin)} in ~/.gemini/bin has no backup — nothing to restore.")
