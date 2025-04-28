from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class unit_hoinhom(BaseModel):
    uid: str
    unit_id: UUID4
    CTNV_ID: int

    class Config:
        from_attributes = True
class hoinhom_unitcreate(unit_hoinhom):
    pass

class hoinhom_unitupdate(unit_hoinhom):
    pass

