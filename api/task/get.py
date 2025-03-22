import uuid

from fastapi import HTTPException
from .router import router, TaskResponse
from db.pg import pg_session
from models.task import Task

@router.get("/{task_id}/", status_code=200, response_model=TaskResponse)
def get_task(task_id: uuid.UUID):
    task = pg_session.query(Task).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return TaskResponse.model_validate(task)
