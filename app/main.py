from fastapi import FastAPI
from datetime import datetime, timezone
from app.api import tasks

app = FastAPI(
    title="DevOps API Lab"
)

@app.get("/health")
async def health():
    return {"status": "ok", "timestamp": datetime.now(timezone.utc)}


app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])
