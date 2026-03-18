from pydantic import BaseModel, ConfigDict


class TaskCreate(BaseModel):
    name: str


class TaskResponse(BaseModel):
    id: int
    name: str
    status: str

    model_config = ConfigDict(
        from_attributes=True
    )