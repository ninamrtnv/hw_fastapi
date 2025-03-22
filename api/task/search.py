from typing import List
from fastapi import HTTPException, Query
from .router import router, TaskResponse
from db.pg import pg_session
from models.task import Task
from functools import lru_cache

@lru_cache(maxsize=50)
@router.get("/search/", status_code=200, response_model=List[TaskResponse])
def search_tasks(query: str = Query(..., min_length=1)):
    try:
        pattern = f"%{query}%"
        tasks = (pg_session.query(Task)
            .filter(
                Task.deleted_at.is_(None),
                (Task.title.ilike(pattern) | Task.description.ilike(pattern))
            ).all()
        )

        res = []
        for task in tasks:
            res.append(TaskResponse(id=str(task.id), title=task.title, description=task.description, priority=task.priority, created_at=task.created_at))

        return res

    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")
