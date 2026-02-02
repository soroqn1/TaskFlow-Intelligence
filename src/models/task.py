from enum import Enum
from pydantic import BaseModel
from typing import Optional

class TaskPriority(str, Enum):
    LOW = "low"
    HIGH = "high"

class TaskBase(BaseModel):
    title: str
    description: str
    priority: TaskPriority

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    priority: Optional[TaskPriority] = None

class Task(TaskBase):
    id: int