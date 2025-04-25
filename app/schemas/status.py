from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class StatusBase(BaseModel):
    name: str
    color: Optional[str] = None


class StatusCreate(StatusBase):
    pass


class StatusUpdate(StatusBase):
    pass


class StatusInDBBase(StatusBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Status(StatusInDBBase):
    pass


class StatusInDB(StatusInDBBase):
    pass 