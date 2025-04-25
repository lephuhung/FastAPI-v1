from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class RelationshipBase(BaseModel):
    name: str


class RelationshipCreate(RelationshipBase):
    pass


class RelationshipUpdate(RelationshipBase):
    pass


class RelationshipInDBBase(RelationshipBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Relationship(RelationshipInDBBase):
    pass


class RelationshipInDB(RelationshipInDBBase):
    pass 