from fastapi import APIRouter
from pydantic import BaseModel, ConfigDict
from datetime import datetime

router = APIRouter(prefix="/task", tags=["task"])


class TaskResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: str
    priority: int
    created_at: datetime

