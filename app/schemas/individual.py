from typing import Optional, List
from pydantic import BaseModel, UUID4
from datetime import datetime, date


class IndividualBase(BaseModel):
    full_name: str
    id_number: Optional[str] = None
    image_url: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_male: Optional[bool] = None
    hometown: Optional[str] = None
    kols_type: Optional[str] = None
    additional_info: Optional[str] = None
    phone_number: Optional[str] = None
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