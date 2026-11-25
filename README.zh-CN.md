<div align="center">
    <a href="https://www.youtube.com/@avencores/" target="_blank">
      <img src="https://github.com/user-attachments/assets/338bcd74-e3c3-4700-87ab-7985058bd17e" alt="YouTube" height="40">
    </a>
    <a href="https://t.me/avencoresyt" target="_blank">
      <img src="https://github.com/user-attachments/assets/939f8beb-a49a-48cf-89b9-d610ee5c4b26" alt="Telegram" height="40">
    </a>
    <a href="https://vk.ru/avencoresreuploads" target="_blank">
      <img src="https://github.com/user-attachments/assets/dc109dda-9045-4a06-95a5-3399f0e21dc4" alt="VK" height="40">
    </a>
    <a href="https://dzen.ru/avencores" target="_blank">
      <img src="https://github.com/user-attachments/assets/bd55f5cf-963c-4eb8-9029-7b80c8c11411" alt="Dzen" height="40">
    </a>
</div>

# 🔑 Open AG Patcher

**[俄文原版（README.md）](README.md)**

<p align="center">
  <a href="https://github.com/AvenCores/open-antigravity-patcher"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=for-the-badge" alt="GPL-3.0 License"></a>
  <a href="https://github.com/AvenCores/open-antigravity-patcher/releases/latest"><img src="https://img.shields.io/github/v/release/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="Latest release"></a>
  <a href="https://github.com/AvenCores/open-antigravity-patcher/stargazers"><img src="https://img.shields.io/github/stars/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="GitHub stars"></a>
  <img src="https://img.shields.io/github/forks/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="GitHub forks">
  <a href="https://github.com/AvenCores/open-antigravity-patcher/watchers">
  <img src="https://img.shields.io/github/watchers/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="GitHub Watchers"></a>
  <a href="https://github.com/AvenCores/open-antigravity-patcher/releases"><img src="https://img.shields.io/github/downloads/AvenCores/open-antigravity-patcher/total?style=for-the-badge" alt="Downloads"></a>
  <a href="https://github.com/AvenCores/open-antigravity-patcher/pulls"><img src="https://img.shields.io/github/issues-pr/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="GitHub pull requests"></a>
  <a href="https://github.com/AvenCores/open-antigravity-patcher/issues"><img src="https://img.shields.io/github/issues/AvenCores/open-antigravity-patcher?style=for-the-badge" alt="GitHub issues"></a>
</p>

面向 Antigravity 2.0、Antigravity IDE、Antigravity CLI 以及 Google Antigravity 的 VS Code 扩展的开源补丁程序：无需 VPN、无需更改 Google 账号所在地区即可解除地区限制。它是工具 [Antigravity IDE 在俄罗斯无需 VPN 和更改 Google 账号地区](https://github.com/confeden/Antigravity) 的开源替代品。

![maxresdefault](https://i.ibb.co/s9Vh80CM/python-w-TPlox-Po-G4.png)

# 🎦 安装与故障排除视频指南

![maxresdefault](https://github.com/user-attachments/assets/54c4f1bd-01f5-4ee8-92d1-f7bbb910d079)

<div align="center">

[**在 YouTube 观看**](https://youtu.be/GyQVTxgt12E)

[**在 Rutube 观看**](https://rutube.ru/video/aba4484f8e0b5e67e966ff8229385f83/)

[**在 Dzen 观看**](https://dzen.ru/video/watch/6a7c430575822e0e4ba2970e)

[**在 VK Video 观看**](https://vkvideo.ru/video-234234162_456239108)

[**在 Telegram 观看**](https://t.me/avencoreschat/571689)

</div>

## ⚠️ HTTP 500 Internal Server Error 错误
如果在 Antigravity IDE 中发起请求时出现 HTTP 500 Internal Server Error 错误，那么没有别的办法，只能更换账号（最好换到 Antigravity IDE 正式可用或已购买付费订阅的地区），付费工具同样无法解决这个问题。

**错误示例**
```
Trajectory ID: 2669b09c-1d11-4620-9bfa-6ad1f0e26a88
Error: HTTP 500 Internal Server Error
Sherlog: 
TraceID: 0xd9ada64bcca3260c
Headers: {"Alt-Svc":["h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000"],"Content-Length":["109"],"Content-Type":["text/event-stream"],"Date":["Sat, 14 Mar 2026 13:51:24 GMT"],"Server":["ESF"],"Server-Timing":["gfet4t7; dur=423"],"Vary":["Origin","X-Origin","Referer"],"X-Cloudaicompanion-Trace-Id":["d9ada64bcca3260c"],"X-Content-Type-Options":["nosniff"],"X-Frame-Options":["SAMEORIGIN"],"X-Xss-Protection":["0"]}

{
  "error": {
    "code": 500,
    "message": "Internal error encountered.",
    "status": "INTERNAL"
  }
}
```

## ⚠️ HTTP 403 Forbidden / SUBSCRIPTION_REQUIRED (#3501) / Agent execution terminated due to error 错误
如果在 Antigravity IDE 或 CLI（`agy`）中出现 `HTTP 403 Forbidden` 错误，原因为 `SUBSCRIPTION_REQUIRED`，或提示 `You do not have a valid license of this product` 或 `Agent execution terminated due to error`，这既不是本地补丁的问题，也不是 `Eligibility Check` 界面。

此错误与 Google API 及用户账号状态有关：许可证、访问权限或 Google 侧的权限校验。补丁程序只修改 Antigravity/Antigravity CLI 的本地文件，无法为账号授予许可证，也无法改变 Google API 的响应，因此它无法解决此错误。

**解决方案：**
1. **更改 Google 账号所在地区**，或使用在 Antigravity 正式可用地区注册的账号。
2. **如果更改地区无效**，则需要购买官方订阅。

**可用的资费方案（Google AI）：**

*   **Google AI Plus**
    *   **价格：** 每月 445 ₽
    *   **存储空间：** 400 GB
    *   **功能：** 使用 AI 工具高效工作，Gemini 配额提升至 2 倍*。
    *   [订阅 Plus](https://one.google.com/about/google-ai-plans/) | [查看套餐权益](https://one.google.com/about/google-ai-plans/) *（适用条款）*
*   **Google AI Pro**
    *   **价格：** 1 790 ₽/月
    *   **存储空间：** 5 TB
    *   **功能：** 凭借 Gemini 中提升至 4 倍的配额*完成更多工作。
    *   [订阅 Pro](https://one.google.com/about/google-ai-plans/) | [查看套餐权益](https://one.google.com/about/google-ai-plans/) *（适用条款）*
*   **Google AI Ultra**
    *   **价格：** 每月 6 990 ₽ 起
    *   **存储空间：** 20 TB 起
    *   **功能：** 凭借 Gemini 中提升至 20 倍的配额*加速工作流程。
    *   [订阅 Ultra](https://one.google.com/about/google-ai-plans/) | [查看套餐权益](https://one.google.com/about/google-ai-plans/) *（适用条款）*

**错误示例：**
```json
{
  "error": {
    "code": 403,
    "details": [
      {
        "@type": "type.googleapis.com/google.rpc.ErrorInfo",
        "domain": "cloudaicompanion.googleapis.com",
        "metadata": {
          "error_number": "1001",
          "uiMessage": "true"
        },
        "reason": "SUBSCRIPTION_REQUIRED"
      }
    ],
    "message": "You do not have a valid license of this product. Please contact your administrator to request a license. If you are not an enterprise user and believe you are receiving this message as an error, please try using the latest version and logging in again. (#3501)",
    "status": "PERMISSION_DENIED"
  }
}
```

## ⚠️ HTTP 400 Bad Request 错误
如果您收到 `HTTP 400 Bad Request` 错误，并伴有 `User location is not supported for the API use` 消息，这意味着 Google 已将您的位置判定为不受支持的地区。

**重要：** 使用 VPN、代理或其他绕过限制的方法可能被 Google 检测到并导致此错误。Google 正在积极对抗各种绕过手段，如果您的 IP 地址或其他会话参数引起怀疑，访问可能会被封锁。

**解决方案：**
1. 应用补丁（**PATCH → `1`: Antigravity IDE patch**）。补丁程序会在代码层面配置正确的 `isGoogleInternal` 绕过。
2. 如果补丁已经应用，请尝试更换 Google 账号或使用其他 VPN。
3. 尝试使用 **[Xbox DNS](https://xbox-dns.ru/)**、**[dns.malw.link](https://info.dns.malw.link/)**、**[GeoHide](https://dns.geohide.ru:8443/)**（用于在 PC 或路由器上绕过限制的专用 DNS 服务器）。

**错误示例：**
```json
{
  "error": {
    "code": 400,
    "message": "User location is not supported for the API use.",
    "status": "FAILED_PRECONDITION"
  }
}
```

## ⚠️ HTTP 429 Too Many Requests / RESOURCE_EXHAUSTED 错误

在 Antigravity 中发送提示词时出现配额耗尽错误：

```
Error: HTTP 429 Too Many Requests
{
  "error": {
    "code": 429,
    "message": "Resource has been exhausted (e.g. check quota).",
    "status": "RESOURCE_EXHAUSTED"
  }
}
```

带 Sherlog 的完整形式：
```
Error: HTTP 429 Too Many Requests
Sherlog:
TraceID: 0xe83b93ad455d1950
Headers: {"Alt-Svc":["h3=\":443\"; ma=2592000,h3-29=\":443\"; ma=2592000"],"Content-Length":["139"],"Content-Type":["text/event-stream"],"Date":["Sun, 06 Sep 2026 10:44:19 GMT"],"Server":["ESF"],"Server-Timing":["gfet4t7; dur=502"],"Vary":["Origin","X-Origin","Referer"],"X-Cloudaicompanion-Trace-Id":["e83b93ad455d1950"],"X-Content-Type-Options":["nosniff"],"X-Frame-Options":["SAMEORIGIN"],"X-Xss-Protection":["0"]}
```

**解决方案：** 重置 Antigravity 数据文件夹（全新配置 + 新令牌），然后可选地从备份恢复对话。以下是 Windows、macOS 和 Linux 的完整指南。

> **Antigravity 与 Antigravity IDE：** Antigravity 2.0 的数据文件夹名为 `Antigravity`，Antigravity IDE 的数据文件夹名为 `Antigravity IDE`。在下面的命令中请替换为对应的名称。后文为简洁起见统一使用 `Antigravity`。

### Windows（完整指南）

**1.** 完全关闭 Antigravity（托盘 → `Quit` / `退出`，并在任务管理器中确认没有 `Antigravity` 进程）。

**2.** 打开 `%appdata%`（`Win+R` → 输入 `%appdata%` → `Enter`）。找到 `Antigravity` 文件夹后，将其移动到安全位置，例如桌面：
```powershell
Move-Item "$env:APPDATA\Antigravity" "$env:USERPROFILE\Desktop\Antigravity-backup"
```

**3.** 启动 Antigravity，登录，发送一条测试提示词以检查连接。429 错误应当消失。

**4.** 如果一切正常，关闭 Antigravity。

**5.** *（可选，恢复对话）* 我们只需要聊天记录：
- `User\globalStorage`（您的聊天记录）
- `User\workspaceStorage`

Antigravity 在第 3 步启动时已经创建了新的干净文件夹 `%appdata%\Antigravity`。只删除其中的这两个文件夹，然后从备份中复制回来：
```powershell
Remove-Item -Recurse -Force "$env:APPDATA\Antigravity\User\globalStorage"
Remove-Item -Recurse -Force "$env:APPDATA\Antigravity\User\workspaceStorage"

Copy-Item -Recurse "$env:USERPROFILE\Desktop\Antigravity-backup\User\globalStorage" "$env:APPDATA\Antigravity\User\"
Copy-Item -Recurse "$env:USERPROFILE\Desktop\Antigravity-backup\User\workspaceStorage" "$env:APPDATA\Antigravity\User\"
```

> ⚠️ **不要复制**备份中的 `settings.json` 文件，否则会恢复旧的故障配置。

**6.** 启动 Antigravity，检查对话并发送提示词。如果一切正常，删除备份：
```powershell
Remove-Item -Recurse -Force "$env:USERPROFILE\Desktop\Antigravity-backup"
```

### macOS（完整指南）

**1.** 完全关闭 Antigravity（`Cmd+Q`，确认 Dock 中图标下方没有小圆点）。

**2.** 将数据文件夹移动到安全位置：
```bash
mv ~/Library/Application\ Support/Antigravity ~/Desktop/Antigravity-backup
```

**3.** 启动 Antigravity，登录，发送一条测试提示词 —— 429 错误应当消失。

**4.** 如果一切正常，关闭 Antigravity（`Cmd+Q`）。

**5.** *（可选，恢复对话）* Antigravity 在第 3 步启动时已经创建了新的干净文件夹 `~/Library/Application Support/Antigravity`。只删除其中的聊天存储，然后从备份中复制回来：
```bash
rm -rf ~/Library/Application\ Support/Antigravity/User/globalStorage
rm -rf ~/Library/Application\ Support/Antigravity/User/workspaceStorage

cp -a ~/Desktop/Antigravity-backup/User/globalStorage ~/Library/Application\ Support/Antigravity/User/
cp -a ~/Desktop/Antigravity-backup/User/workspaceStorage ~/Library/Application\ Support/Antigravity/User/
```

> ⚠️ **不要复制**备份中的 `settings.json` 文件，否则会恢复旧的故障配置。

**6.** 启动 Antigravity，检查对话并发送提示词。如果一切正常，删除备份：
```bash
rm -rf ~/Desktop/Antigravity-backup
```

### Linux（完整指南）

Linux 上的数据文件夹：`${XDG_CONFIG_HOME:-~/.config}/Antigravity`（通常为 `~/.config/Antigravity`）。

**1.** 完全关闭 Antigravity：
```bash
pkill -f -i antigravity; sleep 2; pgrep -a -i antigravity || echo "closed"
```

**2.** 将数据文件夹移动到安全位置：
```bash
# 标准路径
mv ~/.config/Antigravity ~/Antigravity-backup

# 如果设置了 XDG_CONFIG_HOME：
# mv "${XDG_CONFIG_HOME:-$HOME/.config}/Antigravity" ~/Antigravity-backup
ls -d ~/Antigravity-backup
```

**3.** 启动 Antigravity，登录，发送一条测试提示词 —— 429 错误应当消失。

**4.** 如果一切正常，关闭 Antigravity（第 1 步）。

**5.** *（可选，恢复对话）* Antigravity 在第 3 步启动时已经创建了新的干净文件夹 `~/.config/Antigravity`。只删除其中的聊天存储，然后从备份中复制回来：
```bash
rm -rf ~/.config/Antigravity/User/globalStorage
rm -rf ~/.config/Antigravity/User/workspaceStorage

cp -a ~/Antigravity-backup/User/globalStorage ~/.config/Antigravity/User/
cp -a ~/Antigravity-backup/User/workspaceStorage ~/.config/Antigravity/User/
```

> ⚠️ **不要复制**备份中的 `settings.json` 文件，否则会恢复旧的故障配置。

**6.** 启动 Antigravity，检查对话并发送提示词。如果一切正常，删除备份：
```bash
rm -rf ~/Antigravity-backup
```

### 为什么有效

移动数据文件夹后，Antigravity 会从零创建新配置——新令牌、干净的配额。与已耗尽配额之间的旧绑定会被清除。

### 已应用补丁用户的注意事项

补丁修改的是已安装应用内部的 `main.js`（macOS 上位于 `.app` 包内）——移动数据文件夹时它**不会受到影响**，因此无需重新打补丁。

唯一会被重置的是 `settings.json` 中的 runtime workaround。如果在重置数据后出现问题，请再次运行补丁程序（菜单第 1 项）。补丁程序会发现 `main.js` 已被打补丁，并且只应用 settings workaround。

## ⚠️ Antigravity CLI 许可证错误 (#3501)
如果 Antigravity CLI（`agy`）中出现 `You do not have a valid license of this product` 错误，这既不是本地补丁的问题，也不是 `Eligibility Check` 界面。

此错误与 Google API 及用户账号状态有关：许可证、访问权限或 Google 侧的权限校验。补丁程序只修改 Antigravity/Antigravity CLI 的本地文件，无法为账号授予许可证，也无法改变 Google API 的响应，因此它无法解决此错误。

**错误示例：**
```text
⚠ You do not have a valid license of this product. Please contact your administrator to request a license. If you are
not an enterprise user and believe you are receiving this message as an error, please try using the latest version and
logging in again. (#3501)
Error ID: b2c1d9edcaac4fd5ac5766de06c2253b
Trajectory ID: d3ee4302-4213-40f9-9ac5-42e83e38a5ce
```

## ⚠️ 补丁错误："✗ isGoogleInternal -> true (auth) — pattern not found"

如果在应用补丁（PATCH → `1`: Antigravity IDE patch）时收到消息：

```text
✗ isGoogleInternal -> true (auth) — pattern not found
```

这意味着补丁程序在它尝试打补丁的 `main.js` 文件中没有找到预期的 `isGoogleInternal` 模式。

**几乎 100% 的情况是因为补丁程序找到并试图打补丁的是一个随机的 `main.js` 文件，与 Antigravity IDE 无关。**

### 解决方案：

1. 在补丁程序主菜单中检查实际确定的是哪个 `main.js` 文件路径（通常会在开始打补丁前输出）。
2. 确认该路径指向真实的 Antigravity IDE 文件，例如：
   - Windows：`%LOCALAPPDATA%\Programs\Antigravity IDE\resources\app\out\main.js`
   - Linux：`/usr/share/antigravity-ide/resources/app/out/main.js`
   - macOS：`/Applications/Antigravity IDE.app/Contents/Resources/app/out/main.js`
3. 如果路径指向其他文件（例如来自其他 Electron 应用的 `main.js`，或脚本当前目录中的 `main.js`），请选择 **TOOLS → `11` (Select custom path)** 并手动指定 Antigravity IDE 文件夹的正确路径。
4. 确认补丁程序的工作目录中没有无关的 `main.js` 文件——如果存在，补丁程序可能误用它而不是正确的文件（搜索从当前目录开始）。

> **注意：** 如果您从存在其他 `main.js`（例如来自其他项目）的文件夹中运行补丁程序，请将脚本移动到另一个目录，或通过命令行参数显式指定 Antigravity IDE 的路径：
>
> ```bash
> python main.py "C:\Users\<username>\AppData\Local\Programs\Antigravity IDE"
> ```

## 📚 错误的补充信息
如需更深入地了解 HTTP 错误类型及其诊断方法，建议阅读以下指南：
- [5xx Server Errors: The Complete Guide](https://komodor.com/learn/5xx-server-errors-the-complete-guide/) —— 服务器错误的详细解析。

## 🌟 功能
- 自动在标准路径和 Windows 注册表中查找已安装的 Antigravity 2.0、Antigravity IDE、Antigravity CLI（`agy`）以及 Google Antigravity 的 VS Code 扩展。
- **更新检查** —— 启动时自动检查新版本，也可通过菜单手动检查（TOOLS → `9`）。
- **Antigravity CLI 补丁** —— 移除「Eligibility Check」界面，并针对 x86-64 和 ARM64 架构，通过字节签名在机器码层面绕过 Go 二进制文件 `agy`/`agy.exe` 中的 eligibility 检查（支持备份和回滚）。
- **Antigravity Manager（`language_server`）补丁** —— 针对 x86-64 和 ARM64 架构，通过字节签名在后端编译二进制文件中移除授权检查（`hasValidAuth=true`）（支持备份和回滚）。
- **Google Antigravity 的 VS Code 扩展补丁** —— 在 `google.google-antigravity` 扩展的 `extension.js` 中注入防止二进制文件被重复下载的 guard + 禁用 release 渠道变更检查（`isChannelChanged -> false`），使已下载/已打补丁的二进制文件不会被覆盖。此外还会在一次写入中补丁 `~/.gemini/bin/agy` 的两个独立 gate：eligibility 页面和 `agy --hub` 登录所需的 `hasValidAuth`。
- 支持 Linux：在 `/usr/share/antigravity-ide` 中搜索，通过 `dpkg`、`rpm` 和 `package.json` 确定版本。
- 支持 macOS：在 `/Applications` 和 `~/Applications` 中搜索 `.app` 包，修改 `main.js` 后进行 ad-hoc 重签名。
- 修改前创建备份。
- **POSIX 上的原子二进制替换** —— Linux/macOS 上的 `agy` 和 `language_server` 通过同一目录中的临时文件（`tempfile.mkstemp`，O_EXCL）和 `os.replace` 写入：运行中的进程不会阻塞补丁（不会因二进制被占用而出现 `ETXTBSY` / 「Permission denied」），文件保留权限（`+x` 不会丢失）以及原文件的 owner/group；任何错误发生时都会删除临时文件，并且拒绝为符号链接打补丁。公共逻辑位于 `source/patcher/utils/atomic.py`。
- 通过简单菜单应用和回滚补丁。
- 支持 `resources/app/out/main.js` 和 `resources/app/main.js` 路径。
- 彩色输出，并尝试自动提升权限（Windows 上的 UAC，Linux 上提示 `sudo`）。
- 应用补丁前检查 Antigravity IDE 的最低版本（>= `2.1.1`）。
- 通过 Windows 注册表、Linux 包管理器或 macOS 上的 `package.json` 确定 Antigravity IDE 版本。
- 检测已应用的补丁，并提示重新应用。

## 🚀 使用方法
1. 关闭 Antigravity IDE 或 Antigravity 2.0。
2. 以管理员身份运行补丁程序（如有必要，脚本会自行请求提升权限）。
3. 在菜单中选择所需操作：

| 菜单项 | 说明 |
|---|---|
| **PATCH** | |
| `1` Antigravity IDE patch | 为 Antigravity IDE 对 `main.js` 应用补丁（bypass region lock） |
| `2` Antigravity 2.0 patch | 为 `language_server` 二进制文件应用补丁（Antigravity Manager） |
| `3` Antigravity CLI (agy) patch | 为 `agy`/`agy.exe` 二进制文件应用补丁（unlock agy tool） |
| `4` Antigravity VS Code Patch | 补丁 `google.google-antigravity` 扩展的 `extension.js` 及 `~/.gemini/bin/agy` 的两个 gate：eligibility 和 `hasValidAuth` |
| **RESTORE** | |
| `5` Antigravity IDE | 从备份恢复 Antigravity IDE 的原始 `main.js` |
| `6` Antigravity 2.0 | 从备份恢复原始 `language_server` |
| `7` Antigravity CLI | 从备份恢复原始 `agy`/`agy.exe` |
| `8` Antigravity VS Code extension | 从备份恢复原始 `extension.js`（以及 `~/.gemini/bin` 中的二进制文件） |
| **TOOLS** | |
| `9` Check for updates | 检查 GitHub 上的新版本 |
| `10` Open GitHub repository | 在浏览器中打开项目页面 |
| `11` Select custom path | 手动选择应用文件夹或文件路径（IDE / 2.0 / CLI / VS Code extension） |
| `12` About program | 显示程序和作者信息 |
| **`0` Exit** | 退出补丁程序 |

从源码运行：
```bash
python main.py
```

指定路径运行（适用于 Antigravity IDE、Antigravity 2.0 或 Antigravity CLI）：
```bash
# Windows
python main.py "C:\\Users\\<username>\\AppData\\Local\\Programs\\Antigravity IDE"
python main.py "C:\\Users\\<username>\\AppData\\Local\\Programs\\Antigravity\\resources\\bin\\language_server.exe"
python main.py "C:\\Users\\<username>\\AppData\\Local\\agy\\bin\\agy.exe"

# Linux
python main.py /usr/share/antigravity-ide
python main.py /opt/Antigravity/resources/bin/language_server
python main.py /usr/local/bin/agy

# macOS
python3 main.py /Applications/Antigravity\ IDE.app
python3 main.py /Applications/Antigravity.app
python3 main.py /usr/local/bin/agy
```

如果 `main.js` 或 `language_server` 位于脚本旁边，则无需指定路径 —— 它们会被自动找到。

> **macOS：** 如果 `Antigravity IDE.app` 位于 `/Applications`，写入将需要 `sudo`（脚本会自行提示重启）。安装到 `~/Applications` 或用户目录时不需要 `sudo`。补丁成功后，`.app` 会自动使用 ad-hoc 签名重新签名（`/usr/bin/codesign --force --deep --sign -`）—— 否则带 Hardened Runtime 的 Electron 在 macOS 上将无法启动。对已签名 Mach-O 的扫描通过读入内存完成（不使用 `mmap`），以免内核对已经打过补丁的二进制文件进行检查时以 CODESIGNING SIGKILL 终止进程。`com.apple.quarantine` 的移除由内置工具 `/usr/bin/xattr` 完成 —— 不需要额外的 Python 包。

### 🍎 在 macOS 上使用

由于官方发布版本中没有现成的 macOS 二进制构建（仅提供 Windows 和 Linux），您可以直接从源码运行补丁程序，也可以自行构建可执行文件。

#### 方案 1：从源码运行（推荐）
1. 创建虚拟环境、激活并安装必要的依赖：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. 完全关闭 Antigravity 2.0 或 Antigravity IDE。
3. 指定应用路径运行补丁程序：
   ```bash
   # 适用于 Antigravity IDE
   python3 main.py "/Applications/Antigravity IDE.app"
   
   # 适用于 Antigravity 2.0
   python3 main.py "/Applications/Antigravity.app"
   ```
   *注意：如果应用位于 `/Applications` 文件夹中，脚本会自动请求提升权限（`sudo`）以进行写入。*

#### 方案 2：自行构建二进制文件
如果您需要现成的可执行文件，可以按照 [🛠️ 构建](#%EF%B8%8F-构建) 一节的说明自行构建。

构建成功后，通过终端运行编译后的文件：
```bash
cd dist
chmod +x Open_AG_Patcher_macOS
sudo ./Open_AG_Patcher_macOS
```
如果 macOS 阻止运行编译后的文件，请移除 quarantine 属性：
```bash
xattr -dr com.apple.quarantine Open_AG_Patcher_macOS
```

#### 菜单中应选择什么
使用：
- **PATCH → `1`**（Antigravity IDE patch）用于 `Antigravity IDE.app`
- **PATCH → `2`**（Antigravity 2.0 patch）用于 `Antigravity.app`（后端 language_server）
- **PATCH → `3`**（Antigravity CLI (agy) patch）用于 `agy` 二进制文件（如果已安装）
- **PATCH → `4`**（Antigravity VS Code Patch）用于 VS Code 中的 `google.google-antigravity` 扩展
- **RESTORE → `5`**、`6`、`7` 或 `8` 从备份恢复

对于 `Antigravity.app`，补丁程序通常会自动找到：
```text
/Applications/Antigravity.app
```
如果自动搜索没有找到应用，请选择 **TOOLS → `11`**（Select custom path）并指定以下路径之一：
```text
/Applications/Antigravity.app
/Applications/Antigravity IDE.app
```

#### 检查签名
补丁后 `.app` 会自动使用 ad-hoc 签名重新签名。可以通过以下命令检查：
```bash
codesign -dv /Applications/Antigravity.app 2>&1 | grep Signature
```
预期结果：
```text
Signature=adhoc
```

## ❓ 具体修改了什么

### Antigravity IDE 补丁

补丁程序修改 `main.js` 以绕过 `isGoogleInternal` 检查。修改可通过备份（`main.js.bak`）还原。

### `resetIsTierGCPTos(),this.XXX.isGoogleInternal` → `resetIsTierGCPTos(),true`
将授权服务中 `resetIsTierGCPTos()` 调用后的 `isGoogleInternal` 标志检查替换为无条件 `true`，从而激活 Google 的内部访问路径。应用补丁后会自动清理 VS Code 缓存文件夹（`CachedData` 和 `Code Cache/js`），强制 IDE 重新编译已打补丁的 JS 代码。


### Antigravity Manager（language_server）补丁

Antigravity Manager（`language_server` 或 `language_server.exe`）是运行在 Antigravity 2.0 内部的后端服务。默认情况下，它要求通过 Google 侧的授权和许可证校验。

补丁程序通过 `MultiGate` 类，按字节签名直接修改编译后的 `language_server` 二进制文件，支持两种架构：
- **x86-64**（Intel Mac / Windows / Linux x64）：找到并将检查 `cmp byte ptr [rax + 8], 0` 替换为 `mov byte ptr [rax + 8], 1` 并随后填充 `nop`（`\xc6\x40\x08\x01\x90\x90`）。
- **ARM64**（Linux arm64 / Apple Silicon macOS）：找到并将序列 `ldrb w3, [x0, #8] ; tbz w3, #0, skip`（考虑一条或两条准备指令）替换为 `mov w3, #1 ; strb w3, [x0, #8]`（`\x23\x00\x80\x52\x03\x20\x00\x39`）。

结果，`hasValidAuth` 的返回值始终被强制设为 `true`，从而解除封锁。
补丁可通过 **RESTORE → `6`** 从 `.agybak` 恢复原始二进制文件来回滚。
POSIX 上的写入与 `agy` 一样是原子操作（临时文件 + `os.replace`，保留 `+x` 和所有者），运行中的 `language_server` 不会阻塞补丁。

### Antigravity CLI（agy）补丁

Antigravity CLI 是一个独立的 Go 二进制文件（Windows 上为 `agy.exe`，Linux/macOS 上为 `agy`），它会显示一个装饰性的「Eligibility Check」界面，并根据服务器响应生成「Account ineligible」错误。由于它是编译后的二进制文件（不是 JS），补丁通过 `MultiGate` 按唯一字节签名在**机器码层面**针对两种架构执行：**x86-64**（Windows / Linux x64 / Intel Mac）和 **ARM64**（Windows ARM64 / Linux arm64 / Apple Silicon macOS）。

补丁程序应用**一个 gate** —— 在构建错误之前的那个外部检查使错误分支不可达：

#### Gate 1 ——「Eligibility Check」界面

##### x86-64
1. 补丁程序扫描二进制文件，寻找门禁检查的唯一签名：
   ```asm
   test rax, rax              ; 48 85 c0            <-- auth-结果 == nil？
   je  eligible               ; 0f 84 xx xx xx xx   <-- 如果为 nil → GOOD
   cmp byte ptr [rax+8], 0   ; 80 78 08 00         <-- 检查 eligibility 标志
   jne eligible               ; 0f 85 xx xx xx xx   <-- 如果标志 != 0 → GOOD
   call failure_builder       ; e8 xx xx xx xx      <-- BAD：构建错误
   ```
2. 补丁程序将 `cmp byte ptr [rax+8], 0` 替换为 `test rax,rax` + `NOP`（`48 85 c0 90`）。由于此处的 `rax` 一定不为零，`jne` 跳转始终将执行引导到「eligible」分支。
3. CLI 1.5.12 的界面函数还会在调用 helper 前通过 `rcx` 额外检查标志。单独的 gate `eligibility screen off (x64, inline)` 将 `cmp byte ptr [rcx+8],0` 替换为 `test rcx,rcx` + `NOP`（`48 85 c9 90`）。`MultiGate` 会修补这两处 x64 检查；如果缺少内联 gate，即使 helper 已打补丁，`Eligibility check failed:` 界面仍然会出现。

##### ARM64
1. 在当前的本地 arm64 构建中，构建错误前的外部检查如下：
   ```asm
   cbnz x1, error            ; xx xx xx b5     <-- 如果 x1 != 0 → BAD
   cbz  x0, eligible         ; xx xx xx b4     <-- 如果 x0 == 0 → GOOD
   ldrb w1, [x0, #8]        ; 01 20 40 39     <-- 加载 eligibility 标志
   tbnz w1, #0, eligible    ; xx xx xx 37     <-- 如果第 0 位 != 0 → GOOD
   bl   failure_builder      ; xx xx xx 97     <-- BAD：构建错误
   ```
2. 补丁程序将标志加载 `ldrb w1,[x0,#8]` 替换为 `mov w1,#1`（`21 00 80 52`），因此现有的 `tbnz` 始终选择「eligible」分支。`MultiGate` 会自动选择 x64 或 arm64 签名。单一严格的 ARM64 gate 覆盖两种已知尾部：经典形式（`x0`/`x1`/`x2` → `[sp,#0x90]`/`[sp,#0x60]`/`[sp,#0x80]`）以及 macOS 构建中的形式（`x0`/`x1`/`x2`/`x3` → `[sp,#0x98]`/`[sp,#0x60]`/`[sp,#0x88]`/`[sp,#0x58]`）。从 CLI 1.2.7 开始，检查被重新编译，不再有外部 `cbnz`（`cbz x0` → `ldrb w4,[x0,#8]` → `tbnz w4,#0` → `ldp x4,x5,[x0,#0x48]`）—— 它由单独的 gate `eligibility screen off (arm64, w4)` 覆盖，修正为 `mov w4,#1`（`24 00 80 52`）。此外，界面函数中还有一个内联检查（`cbnz x1` → `cbz x0` → `ldrb w2,[x0,#8]` → `tbnz w2,#0` → `bl`）—— 它由 gate `eligibility screen off (arm64, w2)` 覆盖，修正为 `mov w2,#1`（`22 00 80 52`）；如果没有它，即使 w4 已打补丁，`Eligibility check failed:` 界面仍会保留。`MultiGate` 收集**所有**子 gate 的匹配（`resolve_all`）—— 在 1.2.7 中两个位置都会被修补。与最新构建的兼容性由 `test-agy/test_cli_releases.py` 测试自动验证，该测试会下载最新版本的所有归档。

#### 通用步骤
3. 写入前会创建备份 `agy.exe.agybak`（POSIX 上为 `agy.agybak`）。如果现有备份已过期（应用自动更新），它会自动刷新 —— 不保留 stale 副本。
4. 在 Linux/macOS 上写入是原子操作：新字节写入同一目录中的临时文件（`tempfile.mkstemp`，O_EXCL），`fsync` 后通过 `os.replace` 重命名覆盖目标文件，同时保留原文件的权限、所有者和组。运行中的 `agy` 不会妨碍补丁 —— 内核继续执行旧的 inode，后续启动会获得新的二进制文件。在 Windows 上直接写入文件。
5. 在 macOS 上，修改后二进制文件会进行 ad-hoc 重签名（与 `.app` 的情况相同）。

**补丁安全性：**
- 如果在二进制文件中找不到字节签名（未知/不受支持的版本），补丁程序**拒绝打补丁**且不做任何修改 —— 输出「signature not found (unsupported version?)」。
- 写入前每个补丁都会校验：偏移量非负，补丁不超出文件边界且不改变文件大小。
- 禁止为符号链接打补丁：目标必须是普通文件，否则补丁程序拒绝执行写入。
- 如果签名出现多次（Go 可能将同一函数编译为多个实例），补丁程序会对**所有**出现位置应用修正 —— 它们在机器码层面完全相同。
- 回滚通过 **RESTORE → `7`**（Antigravity CLI）从 `.agybak` 恢复完成。

> **平台说明：** x86-64 签名已在 Windows 和 Intel macOS 上验证，ARM64 签名已在 Apple Silicon macOS 上验证。Discovery 跨平台搜索二进制文件（`PATH`、Windows 上的 scoop、POSIX 上的 `/usr/local/bin`、`/opt/antigravity/bin`、`~/.local/bin`）。在 Linux 上 `agy` 二进制文件可能以不同方式编译，签名可能不匹配 —— 在这种情况下，补丁会如实报告，且不修改文件。

### Google Antigravity 扩展（VS Code）补丁

> **⚠️ 重要：** 请使用最新版补丁程序并选择 `PATCH → 4`。仅单独修补 CLI 对 VS Code 不够；此菜单项还会对同一个通过 `--hub` 启动的 `~/.gemini/bin/agy` 应用 `hasValidAuth=true`。如果旧版补丁后登录仍以 `ineligible` 结束，请重新执行菜单 `4`：新认证 gate 会叠加到现有 eligibility 补丁上，同时保留原始 `.agybak`。

VS Code 的 `google.google-antigravity` 扩展每次启动时都会检查后端二进制文件的版本，并从 Google 的 release 服务器重新下载。补丁程序对扩展的 `extension.js` 做两处修改：

#### Part 1 —— 防止重复下载的 guard

在调用 `<receiver>.appendLine('[INSTALL] Checking Antigravity releases...')` 之后注入一个代码块，它检查是否已存在下载好的二进制文件，并**立即返回它**，跳过版本检查和重复下载。在旧的未压缩构建中使用 `targetPathOverride`、`getInstalledTargetPath()` 和字符串返回值：

```js
{const __primary=options.targetPathOverride||getInstalledTargetPath();
const __candidates=[__primary,
(0,path_1.join)((0,path_1.dirname)(__primary),'antigravity'+((0,path_1.extname)(__primary)||''))];
for(const __p of __candidates){if(__p&&await pathExists(__p)){
outputChannel.appendLine('[INSTALL] Existing binary found at '+__p+'. Skipping version check and re-download.');return __p;}}}
```

在压缩构建中（已在 `1.12.0` 上验证）不使用局部变量名：guard 通过 `require('os')`、`require('path')` 和 `require('fs')` 自行计算路径 `~/.gemini/bin/agy[.exe]` 或 `~/.gemini/bin/antigravity[.exe]`。新的 `action` 必须返回对象，因此使用 `return {installPath: __p, fellBackToExisting: false}` 而不是旧的字符串。

插入点的查找依据稳定文本 `[INSTALL] Checking Antigravity releases...`，并匹配**完整调用** `appendLine('...')`，接收者对象名任意 —— 兼容不同的引号、空格和压缩形式，但严格截止到调用的右括号之前，使注入发生在调用之后而不是内部。

#### Part 2 —— 禁用 release 渠道变更检查

```js
// 旧构建：
const isChannelChanged = manifestFetched && lastInstalledUrl !== releaseBaseUrl;
// 改为：
const isChannelChanged = false;

// 压缩构建（变量名 dg 会随版本变化）：
let dg = existingBinaryValid && manifestFetched && channelChanged && !sameChecksum && !keepNewer;
// 改为：
let dg = false;
```

否则扩展会认为 release 渠道已变更，并强制重新下载二进制文件，覆盖已打补丁的版本。在压缩后的 JS 中，所需赋值通过所使用变量的 backreference 以及相邻日志 `[INSTALL] Release channel change detected` 定位，因此短变量名不影响查找。

#### 附加 —— 为已下载的二进制文件打补丁

修补 `extension.js` 后，补丁程序会通过一次扫描和一次写入，对扩展下载的 `~/.gemini/bin/antigravity`（或 `~/.gemini/bin/agy`）应用两个机器码 gate：

1. **Eligibility screen off** —— 禁用本地 eligibility 检查页面。
2. **`hasValidAuth=true`** —— `agy --hub` 模式的 OAuth 登录需要此 gate；缺少它时，授权码交换虽然成功，但 `loadCodeAssist` 仍会以 `failure_kind=ineligible` 结束登录。

普通 CLI 菜单（`PATCH → 3`）仍只应用第一个 gate。如果二进制文件已处于部分补丁状态，现有 `.agybak` 不会被中间状态覆盖；新 gate 会直接追加到当前二进制文件。

**细节：**
- 备份：原文件旁的 `extension.js.vscodebak`；stale 备份会自动刷新。
- 通过存在任一受支持的注入以及渠道检查被禁用来检测已应用的补丁（无论是旧的 `const isChannelChanged = false;` 还是压缩后的 `let <id>=false;`）。
- 回滚：**RESTORE → `8`** 从 `.vscodebak` 恢复 `extension.js`，并提议从 `.agybak` 恢复 `~/.gemini/bin` 中的二进制文件。
- 补丁后需要重新加载 VS Code 窗口（**Developer: Reload Window**）。
- 扩展搜索位置：`~/.vscode/extensions`、`~/.vscode-insiders/extensions`、`~/.vscode-oss/extensions`、`~/.vscode-server/extensions`、`~/.vscode-server-insiders/extensions`（或环境变量 `VSCODE_EXTENSIONS` 指定的目录）。存在多个版本时，选择 mtime 最新的一个。

## 🔍 文件搜索逻辑

补丁程序按以下顺序查找 `main.js`：

1. 命令行参数（目录路径或直接指向 `main.js`）。
2. 当前目录（`./main.js`）。
3. 按标准路径自动搜索：
   - **Windows：**
     - `%LOCALAPPDATA%\Programs\Antigravity IDE`
   - **Linux：**
     - `/usr/share/antigravity-ide`
     - `/opt/Antigravity IDE`
     - `/opt/Antigravity IDE/resources/app/out`
   - **macOS：**
     - `/Applications/Antigravity IDE.app/Contents/Resources/app`
     - `~/Applications/Antigravity IDE.app/Contents/Resources/app`
4. Windows 注册表（`HKCU` 和 `HKLM` 中的 `{AA73B3E3-C6C8-45C8-B1DC-4AE56C751432}_is1` 项：`SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\`）。

在找到的目录内检查以下路径：
- `resources/app/out/main.js`
- `resources/app/main.js`
- `out/main.js`（macOS）
- `main.js`（如果直接指定了路径）

在 macOS 上，脚本也直接接受 `.app` 包路径 —— 会自动解析 `Contents/Resources/app/out/main.js`。

### 搜索 Antigravity CLI（`agy`）

`agy` 二进制文件（Windows 上为 `agy.exe`）采用位置无关的搜索方式 —— 通过 `PATH` 和标准目录，不硬编码路径/版本：

1. 命令行参数或 **TOOLS → `11` → `3`**（`agy`/`agy.exe` 文件路径或文件夹）。
2. `PATH`（`shutil.which("agy")`）。
3. 标准目录：
   - **Windows：** `%LOCALAPPDATA%`、`%PROGRAMFILES%`、`%PROGRAMFILES(X86)%`、`%ProgramData%`、`%APPDATA%`（+ 子目录 `Programs`）、scoop（`%USERPROFILE%\scoop\apps`、`%SCOOP%\apps`）。模式：`agy/bin/agy.exe`、`agy/*/bin/agy.exe`（scoop 版本目录）、`agy*/agy.exe`。
   - **Linux/macOS：** `/usr/local/bin`、`/usr/bin`、`/opt/antigravity/bin`、`/opt/antigravity`、`~/.local/bin`、`~/bin`。

如果找到多个副本（例如 scoop 中存在多个版本），选择 mtime 最新的一个。

### 搜索 Google Antigravity 扩展（VS Code）

`google.google-antigravity` 扩展的 `extension.js` 文件在以下目录中查找（首先是由环境变量 `VSCODE_EXTENSIONS` 覆盖的目录）：

1. 命令行参数或 **TOOLS → `11` → `4`**（`extension.js` 路径、`google.google-antigravity-*` 扩展目录或 `extensions` 根目录）。
2. `~/.vscode/extensions`
3. `~/.vscode-insiders/extensions`
4. `~/.vscode-oss/extensions`
5. `~/.vscode-server/extensions`（远程服务器）
6. `~/.vscode-server-insiders/extensions`

在扩展目录内按掩码 `google.google-antigravity-*` 查找文件夹；存在多个版本时，选择 mtime 最新的一个。预期的文件是扩展目录根部的 `extension.js`。

### 搜索 `~/.gemini/bin` 中的二进制文件

扩展下载的二进制文件（仅由 **PATCH → `4`** 使用）在 `~/.gemini/bin` 中查找：Windows 上为 `antigravity.exe`/`agy.exe`，POSIX 上为 `antigravity`/`agy`。如果那里没有二进制文件，且扩展尚未运行过，补丁程序会提示您在 VS Code 中运行一次扩展，以便它下载二进制文件。

## 🔎 确定 Antigravity IDE 版本

| 平台 | 版本确定方法 |
|---|---|
| **Windows** | 注册表：`{AA73B3E3-...}_is1` 项中的 `DisplayVersion` |
| **Linux (deb)** | `dpkg-query -W antigravity-ide` |
| **Linux (rpm)** | `rpm -q --queryformat %{VERSION} antigravity-ide` |
| **Linux (portable/snap/flatpak)** | `main.js` 旁边的 `package.json` |
| **macOS** | `Antigravity IDE.app/Contents/Resources/app/` 中的 `package.json` |

如果无法确定版本，补丁程序会建议在无检查的情况下继续。如果版本低于 `2.1.1` —— 会发出警告并提供选择。

## 🔒 检查已应用的补丁

打补丁前，脚本通过两个特征检查文件是否已被修补：
- 不存在 `if(this.X.isGoogleInternal)`（模式已替换为 `if(true)`）
- 不存在未修改的 `isGoogleInternal`（基于逗号的授权检查）。

## 🛡️ 权限提升

- **Windows**：通过带 `runas` 参数的 `ShellExecuteW` 自动发起 UAC 请求。能正确处理带空格的路径。
- **Linux**：如果脚本未以 root 运行，会提示通过 `sudo` 重启（`os.execvp`）。如拒绝，则在警告可能发生写入错误的情况下继续。此时 runtime workaround 会写入原始用户的 `settings.json`（`SUDO_USER`/`SUDO_UID`），而不是 `/root/.config/...`。
- **macOS**：使用相同的 posix 分支 —— 未以 root 运行时提示 `sudo`。对于 `~/Applications/Antigravity IDE.app`，可以对 `sudo` 回答「n」（该目录已可写），对于 `/Applications/Antigravity IDE.app` —— 应同意。通过 `sudo` 运行时，用户 `settings.json` 同样取自原始用户的 home，而不是 `root`。

## 🍎 macOS 特性

### 补丁后重签 `.app`

对已签名 `.app` 包内文件的任何修改都会破坏代码签名。启用 Hardened Runtime 的 Electron 应用（Antigravity IDE 就是其中之一）在此之后**无法在 macOS 上启动** —— 甚至在 Gatekeeper 向用户显示对话框之前就会失败。

为了让 `.app` 继续工作，脚本在 `do_patch` 和 `do_restore` 之后会自动执行：

```bash
codesign --force --deep --sign - /path/to/Antigravity\ IDE.app
xattr -dr com.apple.quarantine /path/to/Antigravity\ IDE.app
```

`--sign -` —— ad-hoc 签名（无 Developer ID）。对于本地启动应用来说已经足够。不需要公证（Notarization）。

需要安装 `codesign` —— 它随 **Xcode Command Line Tools** 提供：
```bash
xcode-select --install
```

### 打补丁时出现 "Operation not permitted" 错误

如果您遇到错误 `[!] Backup error: [Errno 1] Operation not permitted: '/Applications/Antigravity IDE.app/Contents/Resources/app/out/main.js.bak'`：

1. 为终端授予完全磁盘访问权限：**系统设置 → 隐私与安全性 → 完全磁盘访问权限**（System Settings → Privacy & Security → Full Disk Access）。
2. 使用以下命令移除应用的隔离属性：
   ```bash
   sudo xattr -rd com.apple.quarantine /path/to/Antigravity\ IDE.app
   ```

### 如果补丁后应用无法启动

1. 确认 `codesign` 可用：`which codesign`。
2. 检查 `.app` 是否已重新签名：`codesign -dv /Applications/Antigravity\ IDE.app 2>&1 | grep Authority` —— 应显示 `Signature=adhoc`。
3. 如果 macOS 仍然阻止：**系统设置 → 隐私与安全性** —— 底部会有「仍要打开」按钮。

## ⚙️ 要求

- **Python** 3.x
- **依赖**：`packaging`（用于版本比较）
- **操作系统**：
  - **Windows** —— 完全支持通过注册表自动搜索和 UAC。
  - **Linux** —— 在 `/usr/share/antigravity-ide` 中自动搜索，通过 `dpkg`/`rpm`/`package.json` 确定版本，sudo 提权。
  - **macOS** —— 在 `/Applications/Antigravity IDE.app` 和 `~/Applications/Antigravity IDE.app` 中自动搜索，通过 `package.json` 确定版本，通过 `codesign` 进行 ad-hoc 重签名（Xcode Command Line Tools）。
- **Antigravity 2.0 最低版本**：`2.5.0`
- **Antigravity IDE 最低版本**：`2.1.1`
- **支持的版本**：Antigravity 2.0 为 `2.3.0` 及以上，IDE 为 `2.1.1` 及以上

## 🛠️ 构建

构建可执行文件建议使用虚拟环境：

1. **创建并激活虚拟环境：**
   * **Windows：**
     ```bash
     cd source
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * **Linux / macOS：**
     ```bash
     cd source
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2. **安装依赖：**
   ```bash
   pip install -r requirements.txt
   ```

3. **通过 PyInstaller 构建：**
   * **Windows：**
     ```bash
     pyinstaller --onefile --uac-admin --icon=icon.ico --name="Open_AG_Patcher_Windows" --noupx --clean --version-file=version.txt main.py
     ```
   * **Linux：**
     ```bash
     pyinstaller --onefile --icon=icon.ico --name="Open_AG_Patcher_Linux" --hidden-import=packaging --hidden-import=packaging.version --hidden-import=packaging.specifiers --hidden-import=packaging.requirements main.py
     ```
   * **macOS (Universal2)：**
     ```bash
     pyinstaller --onefile --name="Open_AG_Patcher_macOS" --target-arch universal2 --hidden-import=packaging --hidden-import=packaging.version --hidden-import=packaging.specifiers --hidden-import=packaging.requirements main.py
     ```

## 项目结构

- `source/main.py` —— 补丁程序的主要入口点（执行访问权限检查并启动 CLI）。
- `source/patcher/` —— 补丁程序的主要源代码，采用模块化架构：
  - `constants.py` —— 全局常量、正则表达式、版本。
  - `cli.py` —— 控制台用户界面、菜单和输入处理。
  - `utils/` —— 系统辅助工具（控制台颜色、管理员权限、POSIX 权限、文件哈希、二进制原子替换 `atomic.py`）。
  - `ide/` —— 查找和修补 Antigravity IDE 本身（`main.js` 文件）的逻辑。
  - `agy/` —— 查找并按字节签名修补 Antigravity CLI（`agy`/`agy.exe`）二进制文件的逻辑。
  - `manager/` —— 查找并按字节签名修补 Antigravity Manager（`language_server`/`language_server.exe`）二进制文件的逻辑。
  - `vscode/` —— 查找和修补 VS Code 的 `google.google-antigravity` 扩展（`extension.js`）及其下载到 `~/.gemini/bin` 的二进制文件的逻辑。
- `source/requirements.txt` —— 构建和运行所需的依赖。
- `source/build.txt` —— 各操作系统构建命令示例。
- `source/icon.ico` —— 用于 `exe`/`app` 的图标。

# 📜 许可证与署名

本项目在 GPL-3.0 许可证下分发。完整许可证文本位于 [`LICENSE`](LICENSE) 文件。

本项目中的部分修改和方案基于 [eligibility-antigravity-patcher](https://github.com/QNIX-Dev/eligibility-antigravity-patcher) 仓库的工作成果，该仓库在 MIT 许可证下分发。所有集成和修改均保留版权并注明原始出处。

---
# 💰 支持作者
+ **SBER**：`2202 2050 1464 4675`
