from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.social_account_link import SocialAccountLink
from app.schemas.social_account_link import SocialAccountLinkCreate, SocialAccountLinkUpdate


class CRUDSocialAccountLink(CRUDBase[SocialAccountLink, SocialAccountLinkCreate, SocialAccountLinkUpdate]):
    def get_by_group_social_account_uid(
        self, db: Session, *, group_social_account_uid: str
    ) -> List[SocialAccountLink]:
        return db.query(SocialAccountLink).filter(SocialAccountLink.group_social_account_uid == group_social_account_uid).all()

    def get_by_linked_social_account_uid(
        self, db: Session, *, linked_social_account_uid: str
    ) -> List[SocialAccountLink]:
        return db.query(SocialAccountLink).filter(SocialAccountLink.linked_social_account_uid == linked_social_account_uid).all()

    def get_active_links(self, db: Session) -> List[SocialAccountLink]:
        return db.query(SocialAccountLink).filter(SocialAccountLink.is_active == True).all()

    def get_by_group_and_linked(
        self, db: Session, *, group_social_account_uid: str, linked_social_account_uid: str
    ) -> Optional[SocialAccountLink]:
        return (
            db.query(SocialAccountLink)
            .filter(
                SocialAccountLink.group_social_account_uid == group_social_account_uid,
                SocialAccountLink.linked_social_account_uid == linked_social_account_uid
            )
            .first()
        )


social_account_link = CRUDSocialAccountLink(SocialAccountLink) 