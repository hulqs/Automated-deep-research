from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import setting
from app.database import init_db
from app.api import auth, users, research, articles, ai, settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield

app = FastAPI(
    title=setting.APP_NAME,
    version=setting.APP_VERSION,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=setting.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(research.router)
app.include_router(articles.router)
app.include_router(ai.router)
app.include_router(settings.router)

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "version": setting.APP_VERSION}
