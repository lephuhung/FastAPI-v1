from typing import Optional
from pydantic import BaseModel


class Role(BaseModel):
    name: Optional[str]

class RoleCreate(Role):
    pass

class RoleUpdate(Role):
    id: int