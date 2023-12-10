from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class doituong_donvi(BaseModel):
    doituong_id: UUID4
    donvi_id: Optional[str]

    class Config:
        from_attributes = True
class doituong_donvicreate(doituong_donvi):
    pass

class doituong_donviupdate(doituong_donvi):
    id: Optional[int]

