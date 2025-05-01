from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.administrator import Administrator
from app.schemas.administrator import AdministratorCreate, AdministratorUpdate


class CRUDAdministrator(CRUDBase[Administrator, AdministratorCreate, AdministratorUpdate]):
    def get_by_uid_administrator(self, db: Session, *, uid_administrator: str) -> Optional[Administrator]:
        return db.query(Administrator).filter(Administrator.uid_administrator == uid_administrator).first()

    def get_by_social_account_uid(self, db: Session, *, social_account_uid: str) -> List[Administrator]:
        return db.query(Administrator).filter(Administrator.social_account_uid == social_account_uid).all()

    def get_by_relationship_id(
        self, db: Session, *, relationship_id: int
    ) -> List[Administrator]:
        return db.query(Administrator).filter(Administrator.relationship_id == relationship_id).all()


administrator = CRUDAdministrator(Administrator) 