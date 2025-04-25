from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.status import Status
from app.schemas.status import StatusCreate, StatusUpdate


class CRUDStatus(CRUDBase[Status, StatusCreate, StatusUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Status]:
        return db.query(Status).filter(Status.name == name).first()

    def get_by_color(self, db: Session, *, color: str) -> List[Status]:
        return db.query(Status).filter(Status.color == color).all()


status = CRUDStatus(Status) 