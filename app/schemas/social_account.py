from typing import Optional, List, Dict, Any
from pydantic import BaseModel
from datetime import datetime


class SocialAccountBase(BaseModel):
    uid: str
    name: str
    reaction_count: Optional[int] = 0
    phone_number: Optional[str] = None
    status_id: Optional[int] = None
    type_id: Optional[int] = None
    note: Optional[str] = None
    is_active: Optional[bool] = True


class SocialAccountCreate(SocialAccountBase):
    pass


class SocialAccountUpdate(SocialAccountBase):
    uid: Optional[str] = None
    name: Optional[str] = None


class SocialAccount(SocialAccountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SocialAccountInDB(SocialAccount):
    """Schema for social account stored in database"""
    pass


class SocialAccountWithRelations(SocialAccount):
    unit: Optional[Dict[str, Any]] = None
    task: Optional[Dict[str, Any]] = None
    status_name: Optional[str] = None

    class Config:
        from_attributes = True 