from typing import Optional, List
from pydantic import BaseModel, UUID4, Field
from datetime import datetime, date
from app.schemas.individual_unit import IndividualUnit, IndividualUnitCreate

class UnitBase(BaseModel):
    id: UUID4
    name: str

class TaskBase(BaseModel):
    id: int
    name: str

class IndividualUnitCreateRequest(BaseModel):
    unit_id: UUID4
    task_id: int

class IndividualBase(BaseModel):
    full_name: str
    national_id: Optional[str] = None
    citizen_id: Optional[str] = None
    image_url: Optional[str] = None
    date_of_birth: date
    is_male: bool
    hometown: str
    additional_info: Optional[str] = None
    phone_number: Optional[str] = None
    is_kol: Optional[bool] = False

class IndividualCreate(IndividualBase):
    individual_units: Optional[List[IndividualUnitCreateRequest]] = None

class IndividualUpdate(IndividualBase):
    unit_id: Optional[UUID4] = None
    task_id: Optional[int] = None

class IndividualInDBBase(IndividualBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class Individual(IndividualInDBBase):
    unit: Optional[UnitBase] = None
    task: Optional[TaskBase] = None

class IndividualInDB(IndividualInDBBase):
    pass 