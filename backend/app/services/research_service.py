import asyncio
import json
import traceback
from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from app.models.research_task import ResearchTask, TaskStatus
from app.models.article import TodoItem, IntermediateReport
from app.models.user import User
from app.models.user_settings import UserSettings
from app.schemas.research import ResearchTaskCreate, ResearchTaskResponse
from app.agents.orchestrator import ResearchOrchestrator

class ResearchService:
    @staticmethod
    async def create_task(db: AsyncSession, user: User, data: ResearchTaskCreate) -> ResearchTask:
        task = ResearchTask(
            user_id=user.id,
            title=data.title,
            topic=data.topic,
            description=data.description,
            status=TaskStatus.PENDING,
        )
        db.add(task)
        await db.commit()
        await db.refresh(task)
        return task

    @staticmethod
    async def get_task(db: AsyncSession, user: User, task_id: str) -> ResearchTask:
        result = await db.execute(
            select(ResearchTask).where(
                ResearchTask.id == task_id,
                ResearchTask.user_id == user.id,
            )
        )
        task = result.scalar_one_or_none()
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    @staticmethod
    async def list_tasks(db: AsyncSession, user: User, skip: int = 0, limit: int = 20):
        result = await db.execute(
            select(ResearchTask)
            .where(ResearchTask.user_id == user.id)
            .order_by(ResearchTask.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        tasks = result.scalars().all()
        count_result = await db.execute(
            select(ResearchTask).where(ResearchTask.user_id == user.id)
        )
        total = len(count_result.scalars().all())
        return tasks, total

    @staticmethod
    async def _load_user_settings(db: AsyncSession, user: User):
        """Load user API settings, or return None to use global defaults."""
        result = await db.execute(
            select(UserSettings).where(UserSettings.user_id == user.id)
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def run_research(db: AsyncSession, user: User, task_id: str) -> ResearchTask:
        task = await ResearchService.get_task(db, user, task_id)
        if task.status not in (TaskStatus.PENDING, TaskStatus.FAILED):
            raise HTTPException(status_code=400, detail=f"Task is already {task.status.value}")

        # Load user's API settings with fallback chain:
        # DB value → global config (.env) → hardcoded default
        from app.config import setting
        us = await ResearchService._load_user_settings(db, user)
        api_key = (us.openai_api_key if us and us.openai_api_key else None) or setting.OPENAI_API_KEY
        base_url = (us.openai_base_url if us and us.openai_base_url else None) or setting.OPENAI_BASE_URL or "https://api.deepseek.com"
        model = (us.openai_model if us and us.openai_model else None) or setting.OPENAI_MODEL or "deepseek-v4-flash"

        orchestrator = ResearchOrchestrator(
            db, task,
            api_key=api_key,
            base_url=base_url,
            model=model,
        )
        try:
            task = await orchestrator.run()
        except Exception as e:
            print(f"[Research ERROR] Task {task_id} failed: {e}")
            traceback.print_exc()
            task.status = TaskStatus.FAILED
            # Reassign dict to ensure SQLAlchemy detects the change
            meta = dict(task.metadata_json or {})
            meta["error"] = str(e)
            task.metadata_json = meta
            await db.commit()
            await db.refresh(task)
        return task

    @staticmethod
    async def delete_task(db: AsyncSession, user: User, task_id: str):
        task = await ResearchService.get_task(db, user, task_id)
        await db.delete(task)
        await db.commit()

    @staticmethod
    async def update_todo(
        db: AsyncSession, user: User, task_id: str, todo_id: str, is_completed: bool
    ) -> TodoItem:
        result = await db.execute(
            select(TodoItem).where(TodoItem.id == todo_id, TodoItem.task_id == task_id)
        )
        todo = result.scalar_one_or_none()
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        todo.is_completed = is_completed
        await db.commit()
        await db.refresh(todo)
        return todo