import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class donvi_hoinhom(Base):
    """
    Database model for an donvi_hoinhom
    """
    __tablename__ = 'donvi_hoinhom'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    donvi_id = Column(UUID(as_uuid=True),ForeignKey("donvi.id"),primary_key=True,nullable=False)
    uid = Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    ctnv_id = Column(Integer, ForeignKey('ctnv.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )