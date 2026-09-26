from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Convert Pydantic validation errors into a flat, human-readable string."""
    messages = []
    for error in exc.errors():
        field = error["loc"][-1] if error["loc"] else "unknown"
        messages.append(f"{field}: {error['msg']}")
    return JSONResponse(
        status_code=422,
        content={"detail": "; ".join(messages)},
    )


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "version": setting.APP_VERSION}
