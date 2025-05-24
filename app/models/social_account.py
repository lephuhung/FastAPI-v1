from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship


class SocialAccount(Base):
    """
    Database model for social account
    """
    __tablename__ = "social_accounts"
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String(100), unique=True, index=True)
    name = Column(String(255))
    reaction_count = Column(Integer, default=0)
    phone_number = Column(String(15))
    status_id = Column(Integer, ForeignKey("statuses.id"))
    type_id = Column(Integer, ForeignKey("account_types.id"))
    note = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    status = relationship("Status", back_populates="social_accounts")
    account_type = relationship("AccountType", back_populates="social_accounts")
    individuals = relationship("IndividualSocialAccount", back_populates="social_account")
    group_statuses = relationship("GroupStatus", back_populates="social_account")
    group_characteristics = relationship("GroupCharacteristic", back_populates="social_account")
    unit_groups = relationship("UnitGroup", back_populates="social_account")
    # reports = relationship("Report", back_populates="social_account")
    group_links = relationship("SocialAccountLink", foreign_keys="[SocialAccountLink.group_social_account_uid]", back_populates="group_social_account")
    linked_links = relationship("SocialAccountLink", foreign_keys="[SocialAccountLink.linked_social_account_uid]", back_populates="linked_social_account")
    administrators = relationship("Administrator", back_populates="social_account") 