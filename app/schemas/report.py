from typing import Optional
from pydantic import BaseModel, Field, UUID4 
import uuid 
from datetime import datetime


class UserBase(BaseModel):
    id: UUID4 
    username: str   

    class Config:
        from_attributes = True


class ReportBase(BaseModel):
    social_account_uid: str 
    content_note: Optional[str] = None 
    comment: Optional[str] = None      
    action: Optional[str] = None       
    related_social_account_uid: Optional[str] = None
    user_id: Optional[UUID4] = None 


class ReportCreate(ReportBase):
    pass


class ReportUpdate(ReportBase):
    pass


class ReportInDB(ReportBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 


class Report(ReportBase): 
    id: int
    created_at: datetime
    updated_at: datetime
    user: Optional[UserBase] = None 

    class Config:
        from_attributes = True 