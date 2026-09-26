#!/bin/sh
# 同时启动两个进程：
#   - FastAPI 后端 (uvicorn)  : 8000  ->  /api/* , /docs
#   - 前端静态服务 (http.server) : 3000  -> index.html + app.js
#
# 前端 app.js 里 API 地址硬编码为 http://localhost:8000/api，
# 因此运行时必须同时映射 3000 与 8000 两个端口。
set -eu

mkdir -p /app/backend/data/uploads /app/backend/data/reports

echo "[entrypoint] starting backend (uvicorn) on 0.0.0.0:8000 ..."
cd /app/backend
python -m uvicorn app.main:app \
    --host 0.0.0.0 \
    --port 8000 \
    --workers "${UVICORN_WORKERS:-1}" &
BACKEND_PID=$!

echo "[entrypoint] starting frontend static server on 0.0.0.0:${FRONTEND_PORT:-3000} ..."
cd /app/frontend
python -m http.server "${FRONTEND_PORT:-3000}" --bind 0.0.0.0 &
FRONTEND_PID=$!

term() {
    echo "[entrypoint] shutting down ..."
    kill -TERM "$BACKEND_PID" "$FRONTEND_PID" 2>/dev/null || true
}
trap term INT TERM

# 任一进程退出即整体退出（docker 会自动重启 / 停止容器）
while kill -0 "$BACKEND_PID" 2>/dev/null && kill -0 "$FRONTEND_PID" 2>/dev/null; do
    sleep 2
done

term
wait 2>/dev/null || true
