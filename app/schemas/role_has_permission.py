from pydantic import UUID4, BaseModel


class Role_has_Permission(BaseModel):
    role_id: UUID4
    permission_id: int

class Role_has_PermissionCreate(Role_has_Permission):
    pass

class Role_has_PermissionUpdate(Role_has_Permission):
    id: int

    