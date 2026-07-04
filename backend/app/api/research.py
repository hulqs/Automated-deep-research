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
            # Ensure the task is marked as failed even if run_research didn't catch it
            try:
                from app.models.research_task import ResearchTask, TaskStatus
                from sqlalchemy import select
                result = await session.execute(
                    select(ResearchTask).where(ResearchTask.id == task_id)
                )
                task = result.scalar_one_or_none()
                if task and task.status != TaskStatus.FAILED:
                    task.status = TaskStatus.FAILED
                    meta = dict(task.metadata_json or {})
                    meta["error"] = str(e)
                    task.metadata_json = meta
                    await session.commit()
            except Exception as inner_e:
                print(f"[Research ERROR] Failed to update task status: {inner_e}")

@router.post("/{task_id}/cancel")
async def cancel_research_task(
    task_id: str,
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Cancel a running research task."""
    from app.models.research_task import TaskStatus
    task = await ResearchService.get_task(db, current_user, task_id)
    if task.status in (TaskStatus.COMPLETED, TaskStatus.FAILED):
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=f"Task is already {task.status.value}")
    task.status = TaskStatus.FAILED
    meta = dict(task.metadata_json or {})
    meta["error"] = "用户取消了研究"
    task.metadata_json = meta
    await db.commit()
    await db.refresh(task)
    return {"detail": "Research cancelled", "task_id": task_id}

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