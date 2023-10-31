from pydantic import UUID4, BaseModel, Datetime, Boolean
from typing import Optional
from datetime import datetime


class doituong(BaseModel):
    id : int
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
    created_at : datetime
    updated_at : datetime
