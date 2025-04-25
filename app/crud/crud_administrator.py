from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.administrator import Administrator
from app.schemas.administrator import AdministratorCreate, AdministratorUpdate


class CRUDAdministrator(CRUDBase[Administrator, AdministratorCreate, AdministratorUpdate]):
    def get_by_facebook_uid(self, db: Session, *, facebook_uid: str) -> Optional[Administrator]:
        return db.query(Administrator).filter(Administrator.facebook_uid == facebook_uid).first()

    def get_by_uid(self, db: Session, *, uid: str) -> List[Administrator]:
        return db.query(Administrator).filter(Administrator.uid == uid).all()

    def get_by_relationship_id(
        self, db: Session, *, relationship_id: int
    ) -> List[Administrator]:
        return db.query(Administrator).filter(Administrator.relationship_id == relationship_id).all()


administrator = CRUDAdministrator(Administrator) 