from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.social_account import SocialAccount
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate


class CRUDSocialAccount(CRUDBase[SocialAccount, SocialAccountCreate, SocialAccountUpdate]):
    def get_by_uid(self, db: Session, *, uid: str) -> Optional[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.uid == uid).first()
    
    def get_all_by_uid(self, db: Session, *, uid: str) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.uid == uid).all()

    def get_by_phone_number(self, db: Session, *, phone_number: str) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.phone_number == phone_number).all()

    def get_by_status(self, db: Session, *, status_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.status_id == status_id).all()

    def get_by_account_type(self, db: Session, *, account_type_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.account_type_id == account_type_id).all()

    def get_linked_accounts(self, db: Session) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.is_linked == True).all()

    def get_all_by_type_id(self, db: Session, *, account_type_id: int) -> List[SocialAccount]:
        """
        Lấy tất cả các social accounts theo account_type_id.
        """
        # Giả định model SocialAccount của bạn có trường tên là 'account_type_id'.
        # Nếu tên trường khác, hãy thay đổi self.model.account_type_id cho phù hợp.
        return db.query(self.model).filter(self.model.account_type_id == account_type_id).all()
    
social_account = CRUDSocialAccount(SocialAccount) 