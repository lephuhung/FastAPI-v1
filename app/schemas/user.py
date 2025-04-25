from typing import Optional, List
from pydantic import BaseModel, UUID4
from datetime import datetime


class UserBase(BaseModel):
    username: str
    is_active: bool = True


class UserCreate(UserBase):
    password: str
    unit_id: Optional[UUID4] = None


class UserUpdate(UserBase):
    password: Optional[str] = None
    unit_id: Optional[UUID4] = None


class UserInDBBase(UserBase):
    id: UUID4
    unit_id: Optional[UUID4] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    hashed_password: str
    salt: str


class UserOutDB(UserBase):
    id: UUID4
    username: Optional[str]
    active: Optional[bool]


class AcessToken(BaseModel):
    access_token: str
    token_type: str


class AcessTokenData(BaseModel):
    id: int
    username: str | None = None
    role: list[str] = []
    permission: list[str] = []
