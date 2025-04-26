from typing import Optional, List
from pydantic import BaseModel, UUID4, Field
from datetime import datetime
import uuid


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    unit_id: str


class UserCreateInDB(UserCreate):
    is_active: bool = False
    salt: str


class UserUpdate(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    unit_id: Optional[UUID4] = None


class UserInDBBase(UserBase):
    id: UUID4
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class User(UserInDBBase):
    pass


class UserInDB(UserInDBBase):
    password: str
    salt: str


class UserOutDB(UserBase):
    id: UUID4
    username: Optional[str]
    is_active: Optional[bool]


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class AccessTokenData(BaseModel):
    id: str
    username: str | None = None
    role: list[str] = []
    permission: list[str] = []


class UserMe(UserInDBBase):
    units: List[dict] = []
    roles: List[dict] = []
    permissions: List[dict] = []
