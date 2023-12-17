from pydantic import  BaseModel
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from datetime import datetime
from typing import Optional

class trichtin(BaseModel):
    uid : Optional[str]
    ghichu_noidung : Optional[str]
    nhanxet : Optional[str]
    xuly: Optional[str]
    uid_vaiao : Optional[str]

    
class trichtinCreate(trichtin):
    pass

class trichtinUpdate(trichtin):
    pass