from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class UnitGroupBase(BaseModel):
    unit_id: UUID4
    social_account_uid: str
    task_id: Optional[int] = None


class UnitGroupCreate(UnitGroupBase):
    pass


class UnitGroupUpdate(UnitGroupBase):
    pass


class UnitGroupInDBBase(UnitGroupBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UnitGroup(UnitGroupInDBBase):
    pass


class UnitGroupInDB(UnitGroupInDBBase):
    pass 