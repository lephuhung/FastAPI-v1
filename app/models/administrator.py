from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship as sa_relationship


class Administrator(Base):
    """
    Database model for administrator
    """
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True)
    uid_administrator = Column(String(100), nullable=False)
    social_account_uid = Column(String(100), ForeignKey("social_accounts.uid", ondelete="CASCADE"), nullable=False)
    relationship_id = Column(Integer, ForeignKey("relationships.id", ondelete="RESTRICT"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    relationship = sa_relationship("Relationship", back_populates="administrators")
    social_account = sa_relationship("SocialAccount", back_populates="administrators") 