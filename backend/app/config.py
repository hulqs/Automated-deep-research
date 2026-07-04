import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Setting(BaseSettings):
    APP_NAME: str = "Deep Research Agent System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./research.db"

    # JWT
    JWT_SECRET_KEY: str = "change-me-in-production-use-a-strong-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    OPENAI_MODEL: str = "deepseek-v4-pro"
    OPENAI_BASE_URL: str = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

    # Search APIs
    WIKIPEDIA_LANG: str = "zh"
    ARXIV_MAX_RESULTS: int = 20

    # CORS
    CORS_ORIGINS: list[str] = ["*"]

    # Storage
    UPLOAD_DIR: str = "./uploads"
    REPORT_DIR: str = "./reports"

    class Config:
        env_file = ".env"
        extra = "allow"

@lru_cache()
def get_settings() -> Setting:
    return Setting()

setting = get_settings()
