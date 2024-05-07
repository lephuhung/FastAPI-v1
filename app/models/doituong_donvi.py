import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Doituong_Donvi(Base):
    """
    Database model for an Doituong UUID
    """
    __tablename__ = 'doituong_donvi'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    doituong_id = Column(UUID(as_uuid=True),ForeignKey("doituong.id"),primary_key=True,nullable=False)
    donvi_id = Column(UUID(as_uuid=True),ForeignKey("donvi.id"),primary_key=True,nullable=False)
    CTNV_ID = Column(Integer, ForeignKey("ctnv.id"), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
