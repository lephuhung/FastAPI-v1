from pydantic import  BaseModel
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from datetime import datetime
from typing import Optional
from pydantic import UUID4
class uid(BaseModel):
    uid : Optional[str]
    name : Optional[str]
    reaction : Optional[int]
    SDT: Optional[str]
    trangthai_id : Optional[int]
    type_id : Optional [int]
    ghichu : Optional[str]
    Vaiao: bool

class uidCreate(uid):
    ctnv_id: Optional[int]
    donvi_id: Optional[UUID4]
    def get_uid_instance(self) -> uid:
        return uid(
            uid=self.uid,
            name=self.name,
            reaction=self.reaction,
            SDT=self.SDT,
            trangthai_id=self.trangthai_id,
            type_id=self.type_id,
            ghichu=self.ghichu,
            Vaiao=self.Vaiao
        )

class uidUpdate(uid):
    pass