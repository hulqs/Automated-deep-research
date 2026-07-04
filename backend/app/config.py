import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

# ---------------------------------------------------------------------------
# Load .env into os.environ BEFORE anything else so that the openai SDK
# (used internally by langchain_openai) can pick up OPENAI_API_KEY and
# OPENAI_BASE_URL. Pydantic-settings only loads values into its own model —
# it does NOT modify os.environ.
# ---------------------------------------------------------------------------
_ENV_FILE = Path(__file__).resolve().parent.parent / ".env"  # backend/.env
if _ENV_FILE.exists():
    # override=True: force .env values to take precedence over system env vars.
    # Without this, pre-existing (possibly empty) system env vars like
    # OPENAI_BASE_URL="" will block .env values from being loaded.
    load_dotenv(_ENV_FILE, override=True)
else:
    # Fallback: try CWD-relative path (keeps backward compatibility)
    load_dotenv(override=True)


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(_ENV_FILE),
        env_file_encoding="utf-8",
        extra="allow",
    )

    APP_NAME: str = "Deep Research Agent System"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite+aiosqlite:///./research.db"

    # JWT
    JWT_SECRET_KEY: str = "change-me-in-production-use-a-strong-secret"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24  # 24 hours

    # API — defaults are overridden by .env values when the file exists
    OPENAI_API_KEY: str = ""
    OPENAI_MODEL: str = "deepseek-v4-flash"
    OPENAI_BASE_URL: str = "https://api.deepseek.com"

    # Search APIs
    WIKIPEDIA_LANG: str = "zh"
    ARXIV_MAX_RESULTS: int = 20

    # CORS
    CORS_ORIGINS: list[str] = ["*"]

    # Storage
    UPLOAD_DIR: str = "./uploads"
    REPORT_DIR: str = "./reports"


@lru_cache()
def get_settings() -> Setting:
    return Setting()


setting = get_settings()
