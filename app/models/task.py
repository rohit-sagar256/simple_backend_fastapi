from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column

from app.database import Base


class Task(Base):
    __tablename__ = "tasks"
    id = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    name = mapped_column(
        String,
        nullable=False,
    )
    status = mapped_column(
        String,
        default="pending",
    )