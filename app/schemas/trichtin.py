from pydantic import  BaseModel
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from datetime import datetime
from typing import Optional
from pydantic import UUID4

class trichtin(BaseModel):
    uid : Optional[str]
    ghichu_noidung : Optional[str]
    nhanxet : Optional[str]
    xuly: Optional[str]
    uid_vaiao : Optional[str]

    
class trichtinCreate(trichtin):
    user_id: UUID4
    

class trichtinUpdate(trichtin):
    pass