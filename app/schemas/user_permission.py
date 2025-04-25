from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class UserPermissionBase(BaseModel):
    user_id: UUID4
    permission_id: int


class UserPermissionCreate(UserPermissionBase):
    pass


class UserPermissionUpdate(UserPermissionBase):
    pass


class UserPermissionInDBBase(UserPermissionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserPermission(UserPermissionInDBBase):
    pass


class UserPermissionInDB(UserPermissionInDBBase):
    pass 