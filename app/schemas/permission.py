from typing import Optional
from pydantic import BaseModel


class Permission(BaseModel):
    name: str
class PermissionCreate(Permission):
    pass
class PermissionUpdate(Permission):
    id: int