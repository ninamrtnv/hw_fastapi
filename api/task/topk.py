from typing import List
from .router import router, TaskResponse
from db.pg import pg_session
from models.task import Task

@router.get("/topk", response_model=List[TaskResponse], status_code=200)
def topk_priority_tasks(k: int = 5):
    query = pg_session.query(Task).filter(Task.deleted_at.is_(None)).order_by(Task.priority.desc()).limit(k)
    tasks = query.all()
    res = []
    for task in tasks:
        res.append(TaskResponse(id=str(task.id), title=task.title, description=task.description, priority=task.priority, created_at=task.created_at))

    return res
