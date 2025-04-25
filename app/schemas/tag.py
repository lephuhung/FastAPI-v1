from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class TagBase(BaseModel):
    name: str
    color: Optional[str] = None


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    pass


class TagInDBBase(TagBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Tag(TagInDBBase):
    pass


class TagInDB(TagInDBBase):
    pass 