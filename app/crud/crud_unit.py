from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitUpdate
from app.models.user_unit import UserUnit


class CRUDUnit(CRUDBase[Unit, UnitCreate, UnitUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Unit]:
        return db.query(Unit).filter(Unit.name == name).first()
    
    def get_by_user_id(self, db: Session, *, user_id: str) -> Optional[Unit]:
        # Lấy user_unit từ bảng user_units
        user_unit = db.query(UserUnit).filter(UserUnit.user_id == user_id).first()
        if not user_unit:
            return None
        
        # Lấy unit từ bảng units
        return db.query(Unit).filter(Unit.id == user_unit.unit_id).first()


unit = CRUDUnit(Unit) 