from typing import List, Optional
from pydantic import BaseModel
from .router import router, TaskResponse
from db.pg import pg_session
from models.task import Task

class FilterTasksRequest(BaseModel):
    byTitle: Optional[bool] = None
    byDescription: Optional[bool] = None
    byCreatedAt: Optional[bool] = None

@router.post("/filter", response_model=List[TaskResponse])
def filter_tasks(request: FilterTasksRequest):
    query = pg_session.query(Task).filter(Task.deleted_at.is_(None))
    if request.byTitle:
        query = query.order_by(Task.title)
    elif request.byDescription:
        query = query.order_by(Task.description)
    elif request.byCreatedAt:
        query = query.order_by(Task.created_at)

    tasks = query.all()
    res = []
    for task in tasks:
        res.append(TaskResponse(id=str(task.id), title=task.title, description=task.description, priority=task.priority, created_at=task.created_at))

    return res
