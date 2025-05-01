from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class AdministratorBase(BaseModel):
    uid_administrator: str
    social_account_uid: str
    relationship_id: int


class AdministratorCreate(AdministratorBase):
    pass


class AdministratorUpdate(AdministratorBase):
    pass


class AdministratorInDBBase(AdministratorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Administrator(AdministratorInDBBase):
    pass


class AdministratorInDB(AdministratorInDBBase):
    pass 