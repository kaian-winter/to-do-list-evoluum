from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    description: str
    due_date: Optional[datetime] = None

class TodoCreate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: UUID
    is_completed: bool
    completed_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
