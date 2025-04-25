from typing import Optional, List
from pydantic import BaseModel, UUID4
from datetime import datetime


class RoleBase(BaseModel):
    name: str


class RoleCreate(RoleBase):
    pass


class RoleUpdate(RoleBase):
    pass


class RoleInDBBase(RoleBase):
    id: UUID4
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class Role(RoleInDBBase):
    pass


class RoleInDB(RoleInDBBase):
    pass