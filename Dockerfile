# syntax=docker/dockerfile:1
#
# Deep Research Agent System — 单镜像多阶段构建
#   Stage 1: 用 Node 把前端 TypeScript 编译成静态 JS
#   Stage 2: Python 运行时，同时跑 FastAPI 后端(:8000) 与前端静态服务(:3000)
#
# 注意: 必须用 Python >= 3.12。backend/app/agents/summarization_agent.py:81
#       在 f-string 表达式中使用了反斜杠（PEP 701），3.11 会 SyntaxError。
#
# 构建:  docker build -t deep-search-agent:latest .
# 运行:  docker run -d --name ds-agent -p 3000:3000 -p 8000:8000 \
#          -e OPENAI_API_KEY=sk-xxx -e JWT_SECRET_KEY=$(openssl rand -hex 32) \
#          -v ds-data:/app/backend/data deep-search-agent:latest

# ---------------------------------------------------------------------------
# Stage 1 — 构建前端 (TypeScript -> JavaScript)
# ---------------------------------------------------------------------------
FROM node:22-alpine AS frontend-build

WORKDIR /build/frontend

# 先只拷贝依赖清单，利用层缓存
COPY frontend/package.json frontend/package-lock.json ./
RUN npm ci

# 再拷贝源码并编译（tsc 输出 app.js 到 frontend 根目录）
COPY frontend/ ./
RUN npm run build

# ---------------------------------------------------------------------------
# Stage 2 — 运行时 (Python + FastAPI + 静态前端)
# ---------------------------------------------------------------------------
FROM python:3.12-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    TZ=Asia/Shanghai \
    DEBUG=false \
    UVICORN_WORKERS=1 \
    FRONTEND_PORT=3000 \
    DATABASE_URL=sqlite+aiosqlite:////app/backend/data/research.db \
    UPLOAD_DIR=/app/backend/data/uploads \
    REPORT_DIR=/app/backend/data/reports

# curl 用于 HEALTHCHECK
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app/backend

# 先装 Python 依赖（依赖不变时可复用缓存）
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 后端源码（.env / *.db / __pycache__ 已被 .dockerignore 排除）
COPY backend/ ./

# 前端构建产物：index.html + 编译出的 app.js（index.html 只引用 app.js）
COPY --from=frontend-build /build/frontend/index.html /app/frontend/
COPY --from=frontend-build /build/frontend/app.js     /app/frontend/

# 启动脚本
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# SQLite 数据库 / uploads / reports 都放在这里 —— 挂卷持久化
RUN mkdir -p /app/backend/data/uploads /app/backend/data/reports
VOLUME ["/app/backend/data"]

EXPOSE 8000 3000

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD curl -fsS http://127.0.0.1:8000/api/health || exit 1

ENTRYPOINT ["docker-entrypoint.sh"]
