from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Unit(Base):
    """
    Database model for unit
    """
    __tablename__ = "units"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(255), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    users = relationship("UserUnit", back_populates="unit")
    individuals = relationship("IndividualUnit", back_populates="unit")
    groups = relationship("UnitGroup", back_populates="unit") 