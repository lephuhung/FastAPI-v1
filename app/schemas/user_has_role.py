from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional

class User_has_Role(BaseModel):
    user_id: UUID4
    role_id: UUID4
class User_has_RoleCreate(User_has_Role):
    pass
class User_has_RoleUpdate(User_has_Role):
    id: int
    pass

