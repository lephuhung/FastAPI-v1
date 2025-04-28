from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, func 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class unit_hoinhom(Base):
    """
    Database model for an unit_hoinhom
    """
    __tablename__ = 'unit_hoinhom'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    unit_id = Column(UUID(as_uuid=True),ForeignKey("unit.id"),primary_key=True,nullable=False)
    uid = Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    CTNV_ID = Column(Integer, ForeignKey('task.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )