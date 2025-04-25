from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class IndividualUnitBase(BaseModel):
    unit_id: UUID4
    individual_id: UUID4
    task_id: Optional[int] = None


class IndividualUnitCreate(IndividualUnitBase):
    pass


class IndividualUnitUpdate(IndividualUnitBase):
    pass


class IndividualUnitInDBBase(IndividualUnitBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class IndividualUnit(IndividualUnitInDBBase):
    pass


class IndividualUnitInDB(IndividualUnitInDBBase):
    pass 