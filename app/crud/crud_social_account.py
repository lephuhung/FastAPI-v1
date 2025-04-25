from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.social_account import SocialAccount
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate


class CRUDSocialAccount(CRUDBase[SocialAccount, SocialAccountCreate, SocialAccountUpdate]):
    def get_by_uid(self, db: Session, *, uid: str) -> Optional[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.uid == uid).first()

    def get_by_phone_number(self, db: Session, *, phone_number: str) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.phone_number == phone_number).all()

    def get_by_status(self, db: Session, *, status_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.status_id == status_id).all()

    def get_by_account_type(self, db: Session, *, account_type_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.account_type_id == account_type_id).all()

    def get_linked_accounts(self, db: Session) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.is_linked == True).all()


social_account = CRUDSocialAccount(SocialAccount) 