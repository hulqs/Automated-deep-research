from sqlalchemy import Column, String, DateTime, Boolean, Text, Enum as SAEnum, ForeignKey, JSON, Integer
from sqlalchemy import func
from sqlalchemy.orm import relationship
from app.database import Base, gen_uuid
import enum
from datetime import datetime

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    RESEARCHER = "researcher"
    USER = "user"

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(100), default="")
    role = Column(SAEnum(UserRole), default=UserRole.USER, nullable=False)
    is_active = Column(Boolean, default=True)
    avatar_url = Column(String(500), default="")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    # Relationships
    research_tasks = relationship("ResearchTask", back_populates="user", cascade="all, delete-orphan")
    articles = relationship("Article", back_populates="author", cascade="all, delete-orphan")
    knowledge_nodes = relationship("KnowledgeNode", back_populates="user", cascade="all, delete-orphan")
    settings = relationship("UserSettings", back_populates="user", uselist=False, cascade="all, delete-orphan")
