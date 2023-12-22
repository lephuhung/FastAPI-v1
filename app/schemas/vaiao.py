from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime, date

class vaiao(BaseModel):
    uid_hoinhom : Optional[str]
    uid_vaiao : Optional[str]
    active : Optional[bool]

class vaiaocreate (vaiao):
    pass

class vaiaoupdate(vaiao):
    pass

class vaiaooutDB(vaiao):
    created_at : datetime
    updated_at: datetime
