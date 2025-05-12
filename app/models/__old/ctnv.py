from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class ctnv(Base):
    """
    Database model for an ctnv
    """
    __tablename__ = 'ctnv'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    name = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )