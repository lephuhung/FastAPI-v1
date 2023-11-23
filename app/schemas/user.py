from datetime import datetime
from typing import Optional

from app.schemas.user_role import UserRole
from pydantic import UUID4, BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username: Optional[str]
    active: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    salt: Optional[str]
    password: str
    created_at: datetime
    updated_at: datetime


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str]
    updated_at: datetime


class UserInDBBase(UserBase):
    id: UUID4
    user_role: Optional[UserRole]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
