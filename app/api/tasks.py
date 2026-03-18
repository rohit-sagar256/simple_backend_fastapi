from fastapi import APIRouter
from app.schemas.task import TaskCreate
from app.tasks.task_worker import process_task

router = APIRouter()

tasks = []


@router.get("/")
async def list_tasks():
    return tasks


@router.post("/")
async def create_task(task: TaskCreate):

    new_task = {
        "id": len(tasks) + 1,
        "name": task.name,
        "status": "pending"
    }

    tasks.append(new_task)

    process_task.delay(task.name)

    return new_task