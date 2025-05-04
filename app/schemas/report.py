from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class ReportBase(BaseModel):
    social_account_uid: str
    content_note: str
    comment: str
    action: str
    related_social_account_uid: Optional[str] = None
    user_id: Optional[UUID4] = None


class ReportCreate(ReportBase):
    pass


class ReportUpdate(ReportBase):
    pass


class UserBase(BaseModel):
    id: str
    name: str


class ReportInDB(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class Report(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime
    user: Optional[UserBase] = None

    class Config:
        orm_mode = True 