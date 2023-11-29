from typing import Any, Dict, List, Optional, Union

from app.core.sercurity import get_password_hash, verify_password
from app.crud.base import CRUDBase

from app.models.donvi import Donvi
from app.schemas.donvi import DonviCreate, DonviUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session
from app.Routes import deps

class CRUDDonvi(CRUDBase[Donvi, DonviCreate, DonviUpdate]):
    # Get User by Name
    def get_donvi_by_name(self, db: Session, *,name: str):
        return db.query(Donvi).filter(Donvi.name==name).first()
    #get user active
    # get user by id
    def get_donvi_by_id(self, db: Session, *, id: UUID4):
        return db.query(Donvi).filter(Donvi.id==id).first()

    # def get_multiple_users_withid(self, db: Session, *,id: int):
    #     return db.query(User).filter(User.id==id).

crud_donvi = CRUDDonvi(Donvi)