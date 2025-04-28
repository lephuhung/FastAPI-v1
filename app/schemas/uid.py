from pydantic import  BaseModel
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from datetime import datetime
from typing import Optional
from pydantic import UUID4
class uid(BaseModel):
    uid : Optional[str]
    name : Optional[str]
    reaction : Optional[int]
    phone_number: Optional[str]
    status : Optional[int]
    account_type_id : Optional [int]
    note : Optional[str]
    Vaiao: bool

class uidCreate(uid):
    task_id: Optional[int]
    unit_id: Optional[UUID4]
    characteristic_id: Optional[int]
    def get_uid_instance(self) -> uid:
        return uid(
            uid=self.uid,
            name=self.name,
            reaction=self.reaction,
            phone_number=self.phone_number,
            status=self.status,
            account_type_id=self.account_type_id,
            note=self.note,
            Vaiao=self.Vaiao
        )

class uidUpdate(uidCreate):
    id_hoinhomunit: Optional[int]
    pass