from datetime import datetime
from typing import Optional

# from app.schemas.user_role import UserRole
from pydantic import UUID4, BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username: Optional[str]


# Properties to receive via API on creation
class UserCreate(UserBase):
    salt: Optional[str]
    active: Optional[bool] = True
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str]
    updated_at: datetime


class UserOutDB(UserCreate):
    username: Optional[str]
    active: Optional[bool]




# Additional properties stored in DB
class UserInDB(UserBase):
    password: str

class AcessToken(BaseModel):
    access_token: str
    token_type: str


class AcessTokenData(BaseModel):
    id: int
    username: str | None = None
    role: list[str] = []
    permission: list[str] = []
