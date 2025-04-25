from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class UnitBase(BaseModel):
    name: str


class UnitCreate(UnitBase):
    pass


class UnitUpdate(UnitBase):
    pass


class UnitInDBBase(UnitBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Unit(UnitInDBBase):
    pass


class UnitInDB(UnitInDBBase):
    pass 