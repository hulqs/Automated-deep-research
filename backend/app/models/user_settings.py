from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy import func
from sqlalchemy.orm import relationship
from app.database import Base, gen_uuid


class UserSettings(Base):
    __tablename__ = "user_settings"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True)
    openai_api_key = Column(Text, default="")
    openai_base_url = Column(String(500), default="https://api.deepseek.com")
    openai_model = Column(String(100), default="deepseek-v4-flash")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="settings")
