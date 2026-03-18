from time import sleep
from app.celery_app import celery_app


@celery_app.task
def process_task(task_name: str):

    print(f"Processing task: {task_name}")

    sleep(5)

    print(f"Finished task: {task_name}")

    return {"status": "completed", "task": task_name}