# 项目长期笔记：deep-search-agent

## 运行方式
- 后端：FastAPI，入口 `backend/app/main.py` 的 `app`，配置在 `backend/app/config.py` + `backend/.env`（相对 `backend/` 读取），SQLite 为 `backend/research.db`（自动建表）。
- 前端：纯 TypeScript 零框架 SPA，`frontend/src/app.ts` 编译到 `frontend/app.js`（`npm run build`）；前端 API 地址硬编码在 `frontend/src/app.ts` 常量 `API = "http://localhost:8000/api"`（约 325 行），改后端地址需改这里并重新 `tsc`。
- **后端 Python 依赖装在项目根目录 `.venv`**，不是 `backend/venv`。用 `..\.venv\Scripts\python.exe` 运行。

## 约定 / 坑
- 项目内多个文件带 UTF-8 BOM（`package.json`、`main.py` 等）。`serve` 包解析 `package.json` 会因 BOM 失败 → 前端静态服务改用 `python -m http.server`。
- **代码实际需要 Python >= 3.12**（`backend/app/agents/summarization_agent.py:81` 在 f-string 表达式里用了 `\\n`，PEP 701，3.11 会 SyntaxError）。README 写的「>=3.11」不准确。
- 容器化：根目录 `Dockerfile`（多阶段：node 编前端 → python:3.12-slim 跑后端）+ `docker-entrypoint.sh`（同时起 uvicorn:8000 与 http.server:3000）+ `.dockerignore` + `docker-compose.yml`。已验证 build/run/健康检查/注册登录全通。
- 本机 Bash 工具不可用；PowerShell 不回显 stdout（需重定向到文件再读）。
- 部署前必须设置 `OPENAI_API_KEY`（及可选 `OPENAI_BASE_URL`/`OPENAI_MODEL`），并修改 `JWT_SECRET_KEY`。
