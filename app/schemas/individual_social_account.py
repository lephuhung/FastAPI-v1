from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class IndividualSocialAccountBase(BaseModel):
    individual_id: UUID4
    social_account_uid: str
    relationship_id: int


class IndividualSocialAccountCreate(IndividualSocialAccountBase):
    pass


class IndividualSocialAccountUpdate(IndividualSocialAccountBase):
    pass


class IndividualSocialAccountInDBBase(IndividualSocialAccountBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class IndividualSocialAccount(IndividualSocialAccountInDBBase):
    pass


class IndividualSocialAccountInDB(IndividualSocialAccountInDBBase):
    pass 