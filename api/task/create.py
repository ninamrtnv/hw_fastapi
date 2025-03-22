from fastapi import HTTPException
from pydantic import BaseModel
from .router import router
from db.pg import pg_session
from models.task import Task

class CreateTaskRequest(BaseModel):
    title: str
    description: str
    priority: int

@router.post("/create", status_code=201)
async def create_track(request: CreateTaskRequest):
    try:
        user_track = Task(title=request.title, description=request.description, priority=request.priority)
        pg_session.add(user_track)
        pg_session.commit()
        return {"message": "ok"}
    except Exception:
        pg_session.rollback()
        raise HTTPException(status_code=500, detail="Internal server error")
