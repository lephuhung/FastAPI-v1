from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.unit import Unit
from app.schemas.unit import UnitCreate, UnitUpdate


class CRUDUnit(CRUDBase[Unit, UnitCreate, UnitUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Unit]:
        return db.query(Unit).filter(Unit.name == name).first()


unit = CRUDUnit(Unit) 