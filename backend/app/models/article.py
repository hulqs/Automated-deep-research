import enum
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, Enum as SAEnum, ForeignKey, JSON, Boolean
from sqlalchemy import func
from sqlalchemy.orm import relationship
from app.database import Base, gen_uuid

class ArticleStatus(str, enum.Enum):
    DRAFT = "draft"
    PUBLISHED = "published"
    ARCHIVED = "archived"

class Article(Base):
    __tablename__ = "articles"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    content = Column(Text, default="")
    abstract = Column(Text, default="")
    keywords = Column(JSON, default=list)
    status = Column(SAEnum(ArticleStatus), default=ArticleStatus.DRAFT, nullable=False)
    source_url = Column(String(500), default="")
    source_type = Column(String(50), default="manual")  # manual, wikipedia, arxiv, web
    file_path = Column(String(500), default="")
    word_count = Column(String(20), default="0")
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())

    author = relationship("User", back_populates="articles")

class KnowledgeNode(Base):
    __tablename__ = "knowledge_nodes"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    task_id = Column(String(36), ForeignKey("research_tasks.id", ondelete="SET NULL"), nullable=True)
    title = Column(String(300), nullable=False)
    content = Column(Text, default="")
    node_type = Column(String(50), default="concept")  # concept, fact, reference, gap
    source = Column(String(500), default="")
    confidence = Column(String(10), default="0.5")
    metadata_json = Column(JSON, default=dict)
    created_at = Column(DateTime(timezone=True), default=func.now())

    user = relationship("User", back_populates="knowledge_nodes")

class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    task_id = Column(String(36), ForeignKey("research_tasks.id", ondelete="CASCADE"), nullable=False)
    content = Column(Text, nullable=False)
    is_completed = Column(Boolean, default=False)
    priority = Column(String(10), default="medium")  # low, medium, high
    order_index = Column(String(10), default="0")
    created_at = Column(DateTime(timezone=True), default=func.now())

    task = relationship("ResearchTask", back_populates="todo_items")

class IntermediateReport(Base):
    __tablename__ = "intermediate_reports"

    id = Column(String(36), primary_key=True, default=gen_uuid)
    task_id = Column(String(36), ForeignKey("research_tasks.id", ondelete="CASCADE"), nullable=False)
    round_number = Column(String(10), default="1")
    content = Column(Text, default="")
    gaps_identified = Column(JSON, default=list)
    created_at = Column(DateTime(timezone=True), default=func.now())

    task = relationship("ResearchTask", back_populates="intermediate_reports")
