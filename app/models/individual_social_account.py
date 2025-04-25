
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Integer, ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class IndividualSocialAccount(Base):
    """
    Database model for individual social account relationship
    """
    __tablename__ = "individual_social_accounts"
    id = Column(Integer, primary_key=True, index=True)
    individual_id = Column(UUID(as_uuid=True), ForeignKey("individuals.id"), index=True)
    social_account_uid = Column(String(255), ForeignKey("social_accounts.uid"), index=True)
    relationship_id = Column(Integer, ForeignKey("relationships.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    individual = relationship("Individual", back_populates="social_accounts")
    social_account = relationship("SocialAccount", back_populates="individuals")
    relationship = relationship("Relationship", back_populates="individual_social_accounts") 