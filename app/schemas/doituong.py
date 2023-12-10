from pydantic import UUID4, BaseModel
from typing import Optional
from datetime import datetime, date

class doituong(BaseModel):
    client_name : Optional[str]
    CMND : Optional[str]
    CCCD : Optional[str]
    Ngaysinh : Optional[date]
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
    id: UUID4
    pass

class doituongoutDB(doituong):
    created_at : datetime
    updated_at: datetime
