from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Individual_Donvi(Base):
    """
    Database model for an Individual UUID
    """
    __tablename__ = 'individual_unit'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    individual_id = Column(UUID(as_uuid=True),ForeignKey("individual.id"),primary_key=True,nullable=False)
    unit_id = Column(UUID(as_uuid=True),ForeignKey("unit.id"),primary_key=True,nullable=False)
    CTNV_ID = Column(Integer, ForeignKey("task.id"), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
