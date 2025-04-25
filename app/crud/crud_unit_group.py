from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.unit_group import UnitGroup
from app.schemas.unit_group import UnitGroupCreate, UnitGroupUpdate
from pydantic import UUID4


class CRUDUnitGroup(CRUDBase[UnitGroup, UnitGroupCreate, UnitGroupUpdate]):
    def get_by_unit_id(self, db: Session, *, unit_id: UUID4) -> List[UnitGroup]:
        return db.query(UnitGroup).filter(UnitGroup.unit_id == unit_id).all()

    def get_by_social_account_uid(
        self, db: Session, *, social_account_uid: str
    ) -> List[UnitGroup]:
        return db.query(UnitGroup).filter(UnitGroup.social_account_uid == social_account_uid).all()

    def get_by_task_id(self, db: Session, *, task_id: int) -> List[UnitGroup]:
        return db.query(UnitGroup).filter(UnitGroup.task_id == task_id).all()

    def get_by_unit_and_social_account(
        self, db: Session, *, unit_id: UUID4, social_account_uid: str
    ) -> Optional[UnitGroup]:
        return (
            db.query(UnitGroup)
            .filter(
                UnitGroup.unit_id == unit_id,
                UnitGroup.social_account_uid == social_account_uid
            )
            .first()
        )


unit_group = CRUDUnitGroup(UnitGroup) 