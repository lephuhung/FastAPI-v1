from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class RolePermissionBase(BaseModel):
    role_id: UUID4
    permission_id: int


class RolePermissionCreate(RolePermissionBase):
    pass


class RolePermissionUpdate(RolePermissionBase):
    pass


class RolePermissionInDBBase(RolePermissionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class RolePermission(RolePermissionInDBBase):
    pass


class RolePermissionInDB(RolePermissionInDBBase):
    pass 