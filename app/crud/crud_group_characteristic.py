from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.group_characteristic import GroupCharacteristic
from app.schemas.group_characteristic import GroupCharacteristicCreate, GroupCharacteristicUpdate


class CRUDGroupCharacteristic(CRUDBase[GroupCharacteristic, GroupCharacteristicCreate, GroupCharacteristicUpdate]):
    def get_by_characteristic_id(self, db: Session, *, characteristic_id: int) -> List[GroupCharacteristic]:
        return db.query(GroupCharacteristic).filter(GroupCharacteristic.characteristic_id == characteristic_id).all()

    def get_by_social_account_uid(
        self, db: Session, *, social_account_uid: str
    ) -> List[GroupCharacteristic]:
        return db.query(GroupCharacteristic).filter(GroupCharacteristic.social_account_uid == social_account_uid).all()

    def get_by_characteristic_and_social_account(
        self, db: Session, *, characteristic_id: int, social_account_uid: str
    ) -> Optional[GroupCharacteristic]:
        return (
            db.query(GroupCharacteristic)
            .filter(
                GroupCharacteristic.characteristic_id == characteristic_id,
                GroupCharacteristic.social_account_uid == social_account_uid
            )
            .first()
        )


group_characteristic = CRUDGroupCharacteristic(GroupCharacteristic) 