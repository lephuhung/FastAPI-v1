from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Donvi(Base):
    """
    Database model for an donvi
    """
    __tablename__ = 'donvi'
    id = Column(UUID(as_uuid=True),primary_key=True,nullable=False, default=uuid4)
    name = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
