from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel
from .router import router
from db.pg import pg_session
from models.task import Task


class TaskUpdateRequest(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[int] = None


@router.put("/{task_id}/", status_code=200)
def update_task(task_id: str, update_data: TaskUpdateRequest):
    task = pg_session.query(Task).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    try:
        if update_data.title is not None:
            task.title = update_data.title
        if update_data.description is not None:
            task.description = update_data.description
        if update_data.priority is not None:
            task.priority = update_data.priority

        pg_session.commit()
        return {"message": "Task updated successfully"}
    except Exception:
        pg_session.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
