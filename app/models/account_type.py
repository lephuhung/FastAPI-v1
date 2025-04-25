
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship


class AccountType(Base):
    """
    Database model for account type
    """
    __tablename__ = "account_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    social_accounts = relationship("SocialAccount", back_populates="account_type") 