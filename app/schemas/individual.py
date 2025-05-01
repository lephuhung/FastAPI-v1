from typing import Optional, List
from pydantic import BaseModel, UUID4, Field
from datetime import datetime, date


class IndividualBase(BaseModel):
    full_name: str
    national_id: Optional[str] = None
    citizen_id: Optional[str] = None
    image_url: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_male: Optional[bool] = None
    hometown: Optional[str] = None
    additional_info: Optional[str] = None
    phone_number: Optional[str] = Field(None, pattern=r'^[0-9]{10,15}$')
    is_kol: bool = False


class IndividualCreate(IndividualBase):
    pass


class IndividualUpdate(IndividualBase):
    pass


class IndividualInDBBase(IndividualBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Individual(IndividualInDBBase):
    pass


class IndividualInDB(IndividualInDBBase):
    pass 