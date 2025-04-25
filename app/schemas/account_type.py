from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class AccountTypeBase(BaseModel):
    name: str


class AccountTypeCreate(AccountTypeBase):
    pass


class AccountTypeUpdate(AccountTypeBase):
    pass


class AccountTypeInDBBase(AccountTypeBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AccountType(AccountTypeInDBBase):
    pass


class AccountTypeInDB(AccountTypeInDBBase):
    pass 