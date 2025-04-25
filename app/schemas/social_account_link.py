from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class SocialAccountLinkBase(BaseModel):
    group_social_account_uid: str
    linked_social_account_uid: str
    is_active: bool = True


class SocialAccountLinkCreate(SocialAccountLinkBase):
    pass


class SocialAccountLinkUpdate(SocialAccountLinkBase):
    pass


class SocialAccountLinkInDBBase(SocialAccountLinkBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class SocialAccountLink(SocialAccountLinkInDBBase):
    pass


class SocialAccountLinkInDB(SocialAccountLinkInDBBase):
    pass 