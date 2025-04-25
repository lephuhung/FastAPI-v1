from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base_class import Base


class SocialAccountLink(Base):
    """
    Database model for social account links
    """
    __tablename__ = "social_account_links"
    id = Column(Integer, primary_key=True, index=True)
    group_social_account_uid = Column(String(100), ForeignKey("social_accounts.uid"), nullable=False)
    linked_social_account_uid = Column(String(100), ForeignKey("social_accounts.uid"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    group_social_account = relationship("SocialAccount", foreign_keys=[group_social_account_uid], back_populates="group_links")
    linked_social_account = relationship("SocialAccount", foreign_keys=[linked_social_account_uid], back_populates="linked_links") 