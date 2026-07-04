import asyncio
import traceback
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models.user import User
from app.core.security import get_current_user
from app.schemas.research import ResearchTaskCreate, ResearchTaskResponse, ResearchTaskListResponse
from app.services.research_service import ResearchService
from app.models.research_task import ResearchTask

router = APIRouter(prefix="/api/research", tags=["Research"])

@router.post("/", response_model=ResearchTaskResponse)
async def create_research_task(
    data: ResearchTaskCreate,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    task = await ResearchService.create_task(db, current_user, data)
    return task

@router.get("/", response_model=ResearchTaskListResponse)
async def list_research_tasks(
    skip: int = 0,
    limit: int = 20,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    tasks, total = await ResearchService.list_tasks(db, current_user, skip, limit)
    return ResearchTaskListResponse(tasks=tasks, total=total)

@router.get("/{task_id}", response_model=ResearchTaskResponse)
async def get_research_task(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await ResearchService.get_task(db, current_user, task_id)

@router.post("/{task_id}/run", response_model=ResearchTaskResponse)
async def run_research_task(
    task_id: str,
    background_tasks: BackgroundTasks,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    task = await ResearchService.get_task(db, current_user, task_id)
    # Run in background
    background_tasks.add_task(_run_research_bg, db, current_user, task_id)
    return task

async def _run_research_bg(db: AsyncSession, user: User, task_id: str):
    from app.database import async_session
    async with async_session() as session:
        try:
            await ResearchService.run_research(session, user, task_id)
        except Exception as e:
            print(f"[Research ERROR] Task {task_id} failed: {e}")
            traceback.print_exc()

@router.delete("/{task_id}")
async def delete_research_task(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await ResearchService.delete_task(db, current_user, task_id)
    return {"detail": "Task deleted"}

@router.put("/{task_id}/todos/{todo_id}")
async def update_todo(
    task_id: str,
    todo_id: str,
    is_completed: bool = True,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await ResearchService.update_todo(db, current_user, task_id, todo_id, is_completed)
    return {"detail": "Todo updated"}