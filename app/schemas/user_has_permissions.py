from pydantic import UUID4, BaseModel

class userhaspermission(BaseModel):
    user_id : UUID4
    Permission_id: int

class userhaspermissionCreate(userhaspermission):
    pass

class userhaspermissionUpdate(userhaspermission):
    id: int