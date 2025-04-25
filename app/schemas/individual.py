from typing import Optional, List
from pydantic import BaseModel, UUID4
from datetime import datetime, date


class IndividualBase(BaseModel):
    client_name: str
    id_number: Optional[str] = None
    image: Optional[str] = None
    date_of_birth: Optional[date] = None
    gender: Optional[bool] = None
    hometown: Optional[str] = None
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