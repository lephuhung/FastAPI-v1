from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class GroupStatusBase(BaseModel):
    status_id: int
    social_account_uid: str


class GroupStatusCreate(GroupStatusBase):
    pass


class GroupStatusUpdate(GroupStatusBase):
    pass


class GroupStatusInDBBase(GroupStatusBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class GroupStatus(GroupStatusInDBBase):
    pass


class GroupStatusInDB(GroupStatusInDBBase):
    pass 