from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from app.config import setting
import uuid
from datetime import datetime

engine = create_async_engine(
    setting.DATABASE_URL,
    echo=setting.DEBUG,
    connect_args={"check_same_thread": False},  # 允许跨线程
)

async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

def gen_uuid():
    return str(uuid.uuid4())

class Base(DeclarativeBase):
    pass

async def get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
