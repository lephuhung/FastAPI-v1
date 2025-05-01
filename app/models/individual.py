from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Date, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Individual(Base):
    """
    Database model for individual
    """
    __tablename__ = "individuals"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    full_name = Column(String(255), nullable=False)
    national_id = Column(String(20))
    citizen_id = Column(String(20))
    image_url = Column(String(255))
    date_of_birth = Column(Date)
    is_male = Column(Boolean)
    hometown = Column(String(255))
    additional_info = Column(String)
    phone_number = Column(String(15))
    is_kol = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    tags = relationship("IndividualTag", back_populates="individual")
    social_accounts = relationship("IndividualSocialAccount", back_populates="individual")
    units = relationship("IndividualUnit", back_populates="individual") 