from typing import Optional
from pydantic import BaseModel, UUID4
from datetime import datetime


class UserRoleBase(BaseModel):
    user_id: UUID4
    role_id: UUID4


class UserRoleCreate(UserRoleBase):
    pass


class UserRoleUpdate(UserRoleBase):
    pass


class UserRoleInDBBase(UserRoleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserRole(UserRoleInDBBase):
    pass


class UserRoleInDB(UserRoleInDBBase):
    pass 