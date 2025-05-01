from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class SocialAccountBase(BaseModel):
    uid: str
    name: str
    reaction_count: int = 0
    phone_number: Optional[str] = None
    status_id: Optional[int] = None
    type_id: Optional[int] = None
    note: Optional[str] = None
    is_active: bool = True


class SocialAccountCreate(SocialAccountBase):
    pass


class SocialAccountUpdate(SocialAccountBase):
    pass


class SocialAccountInDBBase(SocialAccountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SocialAccount(SocialAccountInDBBase):
    pass


class SocialAccountInDB(SocialAccountInDBBase):
    pass 