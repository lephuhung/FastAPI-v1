from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class ReportBase(BaseModel):
    social_account_uid: str
    content_note: Optional[str] = None
    comment: Optional[str] = None
    action: Optional[str] = None
    linked_social_account_uid: Optional[str] = None
    user_id: UUID4


class ReportCreate(ReportBase):
    pass


class ReportUpdate(ReportBase):
    pass


class ReportInDBBase(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Report(ReportInDBBase):
    pass


class ReportInDB(ReportInDBBase):
    pass 