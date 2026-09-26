import enum
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, Enum as SAEnum, ForeignKey, JSON, Integer, Float
from sqlalchemy import func
from sqlalchemy.orm import relationship
from app.database import Base, gen_uuid

class TaskStatus(str, enum.Enum):
    PENDING = "待处理"
    DECOMPOSING = "主题分解"
    SEARCHING = "搜索中"
    SUMMARIZING = "内容总结"
    GENERATING = "报告生成"
    COMPLETED = "完成"
    FAILED = "失败"
    CANCELLED = "已终止"

class ResearchTask(Base):
    __tablename__ = "research_tasks"

    id = Column(String(40), primary_key=True, default=gen_uuid)
    user_id = Column(String(40), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(300), nullable=False)
    topic = Column(Text, nullable=False)
    description = Column(Text, default="")
    status = Column(SAEnum(TaskStatus), default=TaskStatus.PENDING, nullable=False)
    progress = Column(Float, default=0.0)
    queries = Column(JSON, default=list)  # 分解后的搜索查询列表
    search_results = Column(JSON, default=list)  # 收集的搜索结果（如文献元数据）
    knowledge_gaps = Column(JSON, default=list)  # 识别的知识缺口
    summary = Column(Text, default="")  # 阶段性总结
    final_report = Column(Text, default="")  # 最终Markdown报告
    report_path = Column(String(500), default="")  # 报告文件存储路径
    metadata_json = Column(JSON, default=dict)  # 任务元数据（如模型版本、参数配置）
    created_at = Column(DateTime(timezone=True), default=func.now())
    updated_at = Column(DateTime(timezone=True), default=func.now(), onupdate=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    # Relationships
    user = relationship("User", back_populates="research_tasks")
    todo_items = relationship("TodoItem", back_populates="task", cascade="all, delete-orphan")
    intermediate_reports = relationship("IntermediateReport", back_populates="task", cascade="all, delete-orphan")
