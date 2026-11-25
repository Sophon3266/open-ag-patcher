#!/usr/bin/env python3
"""patcher.vscode 针对旧版与压缩版 JS 的回归测试。"""
import os
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "source"))

from patcher.agy import patcher as agy_patcher  # noqa: E402
from patcher.agy.patcher import CLI_GATE, get_status  # noqa: E402
from patcher.utils.atomic import apply_patches_to_data  # noqa: E402
from patcher.vscode import patcher  # noqa: E402


# 旧版扩展片段：未压缩，使用具名变量与固定写法，用于验证旧格式补丁路径。
LEGACY_EXTENSION = """
outputChannel.appendLine('[INSTALL] Checking Antigravity releases...');
const isChannelChanged = manifestFetched && lastInstalledUrl !== releaseBaseUrl;
"""

# VS Code 1.12.0 压缩版片段：变量名被缩短，依赖日志锚点与反向引用定位。
MINIFIED_EXTENSION = """
async function acquire(){return run({action:async()=>{
logger.appendLine("[INSTALL] Checking Antigravity releases...");
var config={};let other=oc!==void 0&&Jb(oc,ob);
let dg=Eb&&Zc&&a&&!Kl&&!d;dg&&(g&&other&&logger.appendLine(`custom URL`),
logger.appendLine(`[INSTALL] Release channel change detected (last installed URL: '${cg}', target URL: '${Ta}'). Forcing backend binary re-download.`));
return{installPath:"downloaded",fellBackToExisting:false};}})}
"""

# 最小的 x64 机器码样例：同时包含资格页面与 hasValidAuth 两个 gate。
CLI_GATE_ORIGINAL = bytes.fromhex(
    "48 85 c0 0f 84 00 00 00 00 80 78 08 00 0f 85 00 00 00 00"
)
AUTH_GATE_ORIGINAL = bytes.fromhex(
    "80 78 08 00 74 10 48 8b 04 24 20 48 89 44 60"
)


class VsCodePatcherTests(unittest.TestCase):
    def apply_patch(self, content):
        """依次应用两部分补丁，返回 (内容, PART 1 状态, PART 2 状态)。"""
        content, status1 = patcher._apply_part1(content)
        content, status2 = patcher._apply_part2(content)
        return content, status1, status2

    def test_minified_extension_patch_and_idempotence(self):
        # 压缩版应被正确改写，且再次应用时两部分都返回 already（幂等）。
        patched, status1, status2 = self.apply_patch(MINIFIED_EXTENSION)

        self.assertEqual((status1, status2), ("applied", "applied"))
        # PART 1 的注入返回值是对象（新构建要求 installPath 字段）。
        self.assertIn("return{installPath:__p,fellBackToExisting:false}", patched)
        # PART 2 只改目标渠道变量 dg，不能误改相邻的 other。
        self.assertIn("let dg=false;", patched)
        self.assertNotIn("let other=false;", patched)
        self.assertTrue(patcher.is_already_patched(patched))
        self.assertEqual(self.apply_patch(patched), (patched, "already", "already"))

    def test_legacy_extension_patch_still_supported(self):
        # 旧版未压缩代码仍应走原始正则路径，且重复应用幂等。
        patched, status1, status2 = self.apply_patch(LEGACY_EXTENSION)

        self.assertEqual((status1, status2), ("applied", "applied"))
        # PART 1 的注入返回字符串，兼容旧版扩展。
        self.assertIn("return __p;", patched)
        self.assertIn("const isChannelChanged = false;", patched)
        self.assertTrue(patcher.is_already_patched(patched))
        self.assertEqual(self.apply_patch(patched), (patched, "already", "already"))

    def test_vscode_status_requires_both_binary_gates(self):
        # 仅修资格页面时，普通 CLI 状态会为 patched，但 VS Code 登录仍未修复。
        data = bytearray(CLI_GATE_ORIGINAL + AUTH_GATE_ORIGINAL)
        cli_patches = []
        for kind, offsets, gate in CLI_GATE.resolve_all(data):
            self.assertEqual(kind, "unpatched")
            cli_patches.extend((offset, gate) for offset in offsets)
        data = apply_patches_to_data(data, cli_patches)

        fd, path = tempfile.mkstemp()
        os.close(fd)
        try:
            with open(path, "wb") as file:
                file.write(data)
            self.assertEqual(get_status(path)[0], "patched")
            self.assertEqual(
                get_status(path, extra_gates=patcher.VSCODE_AGY_EXTRA_GATES)[0],
                "unpatched",
            )

            auth_gate, _ = patcher.VSCODE_AGY_EXTRA_GATES[0]
            auth_patches = []
            for kind, offsets, gate in auth_gate.resolve_all(data):
                self.assertEqual(kind, "unpatched")
                auth_patches.extend((offset, gate) for offset in offsets)
            data = apply_patches_to_data(data, auth_patches)
            with open(path, "wb") as file:
                file.write(data)

            self.assertEqual(
                get_status(path, extra_gates=patcher.VSCODE_AGY_EXTRA_GATES)[0],
                "patched",
            )
        finally:
            os.unlink(path)

    def test_partial_vscode_patch_preserves_original_backup(self):
        # 当前文件只含 CLI 补丁、备份仍为原版时，补 hasValidAuth 不得覆盖备份。
        original = CLI_GATE_ORIGINAL + AUTH_GATE_ORIGINAL
        data = bytearray(original)
        cli_patches = []
        for _kind, offsets, gate in CLI_GATE.resolve_all(data):
            cli_patches.extend((offset, gate) for offset in offsets)
        partial = apply_patches_to_data(data, cli_patches)

        with tempfile.TemporaryDirectory() as directory:
            path = os.path.join(directory, "agy")
            backup = path + ".agybak"
            with open(path, "wb") as file:
                file.write(partial)
            with open(backup, "wb") as file:
                file.write(original)

            # POSIX 的真实补丁流程会复制到用户 bin 并尝试签名；测试中隔离这些副作用。
            with mock.patch.object(agy_patcher, "_copy_to_user_bin"), \
                    mock.patch.object(agy_patcher, "resign_macos_bundle"), \
                    mock.patch.object(agy_patcher, "resign_macos_binary"):
                agy_patcher.do_patch_agy(
                    path,
                    extra_gates=patcher.VSCODE_AGY_EXTRA_GATES,
                )

            with open(backup, "rb") as file:
                self.assertEqual(file.read(), original)
            self.assertEqual(
                get_status(path, extra_gates=patcher.VSCODE_AGY_EXTRA_GATES)[0],
                "patched",
            )

    def test_unknown_extension_is_not_modified(self):
        # 不含锚点的内容必须原样返回，避免误改其他扩展。
        content = "logger.appendLine('[INSTALL] Something else');let value=true;"
        self.assertEqual(self.apply_patch(content), (content, "not-found", "not-found"))
        self.assertFalse(patcher.is_already_patched(content))


if __name__ == "__main__":
    unittest.main()
