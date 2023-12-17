from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class donvi_hoinhom(BaseModel):
    uid: str
    donvi_id: UUID4
    CTNV_ID: int

    class Config:
        from_attributes = True
class hoinhom_donvicreate(donvi_hoinhom):
    pass

class hoinhom_donviupdate(donvi_hoinhom):
    pass

