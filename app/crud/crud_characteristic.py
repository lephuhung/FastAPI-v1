from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.characteristic import Characteristic
from app.schemas.characteristic import CharacteristicCreate, CharacteristicUpdate


class CRUDCharacteristic(CRUDBase[Characteristic, CharacteristicCreate, CharacteristicUpdate]):
    def get_by_name(self, db: Session, *, name: str) -> Optional[Characteristic]:
        return db.query(Characteristic).filter(Characteristic.name == name).first()

    def get_by_color(self, db: Session, *, color: str) -> List[Characteristic]:
        return db.query(Characteristic).filter(Characteristic.color == color).all()


characteristic = CRUDCharacteristic(Characteristic) 