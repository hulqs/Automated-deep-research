import asyncio
import json
import logging
import traceback
from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Query
from fastapi.responses import StreamingResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.database import get_db, async_session
from app.models.user import User
from app.core.security import get_current_user, decode_access_token
from app.schemas.research import ResearchTaskCreate, ResearchTaskResponse, ResearchTaskListResponse
from app.services.research_service import ResearchService
from app.models.research_task import ResearchTask, TaskStatus
from app.schemas.sse_events import format_sse

logger = logging.getLogger(__name__)

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

# ──────────────────────────────────────────────
# SSE streaming endpoint (must be before /{task_id})
# ──────────────────────────────────────────────

@router.get("/{task_id}/stream")
async def stream_research_task(
    task_id: str,
    token: str = Query(..., description="JWT token for EventSource auth (query param)"),
    db: AsyncSession = Depends(get_db),
):
    """SSE endpoint: stream research progress and report generation in real time.

    Uses Server-Sent Events to push phase transitions, token-by-token
    Markdown output, and progress updates to the frontend.

    Auth: accepts JWT as a query parameter because browser EventSource
    does not support custom HTTP headers.
    """
    # ── Auth via query param (EventSource can't set Authorization header) ──
    try:
        payload = decode_access_token(token)
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token: missing sub")
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user or not user.is_active:
            raise HTTPException(status_code=401, detail="User not found or inactive")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Authentication failed: {str(e)}")

    # ── Verify task ownership ──
    task = await ResearchService.get_task(db, user, task_id)

    # ── If task already complete, send result immediately and close ──
    if task.status == TaskStatus.COMPLETED and task.final_report:
        async def send_completed():
            yield format_sse("complete", {
                "task_id": task_id,
                "progress": 1.0,
                "status": "完成",
            })
        return StreamingResponse(
            send_completed(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    # ── If task in terminal error state ──
    if task.status in (TaskStatus.FAILED, TaskStatus.CANCELLED):
        async def send_terminal():
            meta = task.metadata_json or {}
            yield format_sse("error", {"message": meta.get("error", f"Task is {task.status.value}")})
        return StreamingResponse(
            send_terminal(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    # ── If task is already running (started via /run or reconnection),
    #     poll until completion then stream the final report ──
    if task.status not in (TaskStatus.PENDING,):
        async def poll_and_stream():
            from app.database import async_session as session_factory
            from app.utils.stream_chunker import StreamChunker

            yield format_sse("phase", {
                "phase": "reconnecting",
                "progress": task.progress or 0,
                "message": f"Task is already running — waiting for completion...",
            })

            last_progress = task.progress or 0
            async with session_factory() as poll_db:
                # Initial query to get a session-bound instance
                result = await poll_db.execute(
                    select(ResearchTask).where(ResearchTask.id == task_id)
                )
                current = result.scalar_one_or_none()
                if not current:
                    yield format_sse("error", {"message": "Task not found"})
                    return

                while True:
                    await asyncio.sleep(2)
                    try:
                        await poll_db.refresh(current)
                    except Exception:
                        result = await poll_db.execute(
                            select(ResearchTask).where(ResearchTask.id == task_id)
                        )
                        current = result.scalar_one_or_none()
                        if not current:
                            yield format_sse("error", {"message": "Task not found"})
                            return

                    if current.status == TaskStatus.CANCELLED:
                        yield format_sse("cancelled", {"task_id": task_id})
                        return
                    if current.status == TaskStatus.FAILED:
                        meta = current.metadata_json or {}
                        yield format_sse("error", {"message": meta.get("error", "Research failed")})
                        return

                    new_progress = current.progress or 0
                    if new_progress > last_progress:
                        last_progress = new_progress
                        yield format_sse("phase", {
                            "phase": current.status.value if isinstance(current.status, TaskStatus) else str(current.status),
                            "progress": new_progress,
                            "message": f"Progress: {current.status.value if isinstance(current.status, TaskStatus) else current.status}",
                        })

                    if current.status == TaskStatus.COMPLETED and current.final_report:
                        report = current.final_report
                        chunker = StreamChunker(min_chunk=20, max_chunk=80)
                        for i in range(0, len(report), 12):
                            token = report[i:i + 12]
                            for chunk in chunker.feed(token):
                                yield format_sse("token", {"text": chunk, "source": "report"})
                            await asyncio.sleep(0.005)
                        final_chunk = chunker.flush()
                        if final_chunk:
                            yield format_sse("token", {"text": final_chunk, "source": "report"})
                        yield format_sse("complete", {
                            "task_id": task_id,
                            "progress": 1.0,
                            "status": "完成",
                        })
                        return

        return StreamingResponse(
            poll_and_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
                "X-Accel-Buffering": "no",
            },
        )

    # ── Main streaming generator (task is PENDING — start fresh research) ──
    async def event_generator():
        from app.database import async_session as session_factory
        queue: asyncio.Queue = asyncio.Queue(maxsize=256)

        async with session_factory() as research_db:
            research_task = asyncio.create_task(
                ResearchService.run_research_stream(research_db, user, task_id, queue)
            )

            try:
                while True:
                    try:
                        event_type, data = await asyncio.wait_for(
                            queue.get(), timeout=15.0
                        )
                        yield format_sse(event_type, data)

                        if event_type in ("complete", "cancelled", "error"):
                            break

                    except asyncio.TimeoutError:
                        yield format_sse("heartbeat", {"ts": datetime.now(timezone.utc).isoformat()})

                    if research_task.done():
                        while not queue.empty():
                            try:
                                event_type, data = queue.get_nowait()
                                yield format_sse(event_type, data)
                            except asyncio.QueueEmpty:
                                break

                        if research_task.exception():
                            err = research_task.exception()
                            yield format_sse("error", {"message": str(err)})
                        break

            except asyncio.CancelledError:
                logger.info(f"SSE connection cancelled for task {task_id}")
                yield format_sse("error", {"message": "Client disconnected"})
            finally:
                if not research_task.done():
                    research_task.cancel()
                    try:
                        await research_task
                    except asyncio.CancelledError:
                        pass

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",  # Disable nginx buffering
        },
    )


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
    background_tasks.add_task(_run_research_bg, current_user, task_id)
    return task

async def _run_research_bg(user: User, task_id: str):
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
                if task and task.status not in (TaskStatus.FAILED, TaskStatus.CANCELLED, TaskStatus.COMPLETED):
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
    if task.status in (TaskStatus.COMPLETED, TaskStatus.FAILED, TaskStatus.CANCELLED):
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=f"Task is already {task.status.value}")
    task.status = TaskStatus.CANCELLED
    meta = dict(task.metadata_json or {})
    meta["cancelled_at"] = task.updated_at.isoformat() if hasattr(task, 'updated_at') else None
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