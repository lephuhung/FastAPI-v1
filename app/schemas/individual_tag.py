from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class IndividualTagBase(BaseModel):
    individual_id: UUID4
    tag_id: int


class IndividualTagCreate(IndividualTagBase):
    pass


class IndividualTagUpdate(IndividualTagBase):
    pass


class IndividualTagInDBBase(IndividualTagBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class IndividualTag(IndividualTagInDBBase):
    pass


class IndividualTagInDB(IndividualTagInDBBase):
    pass 