from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime

class doituong(BaseModel):
    name : Optional[str]
    CMND : Optional[str]
    CCCD : Optional[str]
    Image : Optional[str]
    Ngaysinh : Optional[datetime]
    # True is Nam, False is Nu
    Gioitinh : bool
    Quequan : Optional[str]
    Thongtinbosung : Optional[str]
    SDT : Optional[str]
    KOL: bool
    Image:Optional[str]

class doituongcreate (doituong):
    pass

class doituongupdate(doituong):
    pass

class doituongoutDB(doituong):
    created_at : datetime
    updated_at: datetime
