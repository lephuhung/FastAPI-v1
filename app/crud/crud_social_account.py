from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.social_account import SocialAccount
from app.schemas.social_account import SocialAccountCreate, SocialAccountUpdate


class CRUDSocialAccount(CRUDBase[SocialAccount, SocialAccountCreate, SocialAccountUpdate]):
    def get_by_uid(self, db: Session, *, uid: str) -> Optional[SocialAccount]:
        return db.query(self.model).filter(self.model.uid == uid).first()

    def get_by_phone_number(self, db: Session, *, phone_number: str) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.phone_number == phone_number).all()

    def get_by_status(self, db: Session, *, status_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.status_id == status_id).all()

    def get_by_account_type(self, db: Session, *, type_id: int) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.type_id == type_id).all()

    def get_active_accounts(self, db: Session) -> List[SocialAccount]:
        return db.query(SocialAccount).filter(SocialAccount.is_active == True).all()

    def get_all_by_type_id(self, db: Session, *, type_id: int) -> List[SocialAccount]:
        return db.query(self.model).filter(self.model.type_id == type_id).all()

    def get_all_by_status_id(self, db: Session, *, status_id: int) -> List[SocialAccount]:
        return db.query(self.model).filter(self.model.status_id == status_id).all()

    def get_by_is_active(self, db: Session, *, is_active: bool) -> List[SocialAccount]:
        return db.query(self.model).filter(self.model.is_active == is_active).all()

    def get_all_by_page_group(self, db: Session, *, type_group: int, type_page: int) -> List[SocialAccount]:
        return db.query(self.model).filter(
            self.model.type_group == type_group,
            self.model.type_page == type_page
        ).all()

    def get_all_by_type_id(self, db: Session, *, account_type_id: int) -> List[SocialAccount]:
        """
        Lấy tất cả các social accounts theo account_type_id.
        """
        # Giả định model SocialAccount của bạn có trường tên là 'account_type_id'.
        # Nếu tên trường khác, hãy thay đổi self.model.account_type_id cho phù hợp.
        return db.query(self.model).filter(self.model.account_type_id == account_type_id).all()
    
social_account = CRUDSocialAccount(SocialAccount) 