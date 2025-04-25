from typing import Any, Dict, Optional, Union, List
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models.individual_social_account import IndividualSocialAccount
from app.schemas.individual_social_account import IndividualSocialAccountCreate, IndividualSocialAccountUpdate
from pydantic import UUID4


class CRUDIndividualSocialAccount(CRUDBase[IndividualSocialAccount, IndividualSocialAccountCreate, IndividualSocialAccountUpdate]):
    def get_by_individual_id(self, db: Session, *, individual_id: UUID4) -> List[IndividualSocialAccount]:
        return db.query(IndividualSocialAccount).filter(IndividualSocialAccount.individual_id == individual_id).all()

    def get_by_social_account_uid(
        self, db: Session, *, social_account_uid: str
    ) -> List[IndividualSocialAccount]:
        return db.query(IndividualSocialAccount).filter(IndividualSocialAccount.social_account_uid == social_account_uid).all()

    def get_by_relationship_id(
        self, db: Session, *, relationship_id: int
    ) -> List[IndividualSocialAccount]:
        return db.query(IndividualSocialAccount).filter(IndividualSocialAccount.relationship_id == relationship_id).all()

    def get_by_individual_and_social_account(
        self, db: Session, *, individual_id: UUID4, social_account_uid: str
    ) -> Optional[IndividualSocialAccount]:
        return (
            db.query(IndividualSocialAccount)
            .filter(
                IndividualSocialAccount.individual_id == individual_id,
                IndividualSocialAccount.social_account_uid == social_account_uid
            )
            .first()
        )


individual_social_account = CRUDIndividualSocialAccount(IndividualSocialAccount) 