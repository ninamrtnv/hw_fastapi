from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.pg import pg_session
from .task.router import router as task_router
from .task import create, delete, filter, search, get, topk, update

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    pg_session.remove()

def create_app() -> FastAPI:
    app = FastAPI(
        title="Task Tracker API v1",
        description="API version 1",
        version="1.0",
        openapi_tags=[
            {"name": "task", "description": "Operations with task"}
        ],
        lifespan=lifespan,
    )

    app.include_router(task_router, prefix="/api/v1")

    return app
