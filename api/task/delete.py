from fastapi import HTTPException
from datetime import datetime
from .router import router
from db.pg import pg_session
from models.task import Task

@router.delete("/{task_id}/", status_code=200)
def delete_task(task_id: str):
    task = pg_session.query(Task).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    try:
        task.deleted_at = datetime.now()
        pg_session.commit()
        return {"message": "ok"}
    except Exception:
        pg_session.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")

