# 游戏开发部的大冒险 · 部署说明

《蔚蓝档案》同人卡牌肉鸽（免费非盈利）。单文件 HTML 原型，GitHub Pages 发布。

## 线上地址
https://lx960902-stack.github.io/star-echo/

## 更新流程（重要）

**本机 git push 会卡死**（receive-pack 上传阶段，即使走代理），必须用 API 脚本部署：

1. 修改 `../index.html`（原型本体）或 `../assets/` 后，把变更复制到本目录：
   ```powershell
   Copy-Item "..\index.html" . -Force
   Copy-Item "..\assets" . -Recurse -Force
   ```
2. 运行部署脚本（GitHub Git Data API：blob → tree → commit → 强制更新 main）：
   ```powershell
   powershell -NoProfile -ExecutionPolicy Bypass -File .\deploy_via_api.ps1
   ```
3. 等待约 1 分钟 GitHub Pages 构建，浏览器验证线上版本。

## 定时任务
- `ba-dev-progress`：每 30 分钟按 `game/开发任务书.md` 自动推进开发（cron）
- 修改代码后若需上线，可手动执行上述步骤；线上版本以 `deploy/` 为准

## 版权
非盈利同人作品，角色版权归原版权方（《蔚蓝档案》/ Nexon & Yostar）。
