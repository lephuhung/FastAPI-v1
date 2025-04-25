
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship


class Relationship(Base):
    """
    Database model for relationship
    """
    __tablename__ = "relationships"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    individual_social_accounts = relationship("IndividualSocialAccount", back_populates="relationship")
    administrators = relationship("Administrator", back_populates="relationship") 