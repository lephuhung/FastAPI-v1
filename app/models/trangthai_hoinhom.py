import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class trangthai_hoinhom(Base):
    """
    Database model for an trangthai_hoinhom
    """

    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    trangthai_id = Column(Integer, ForeignKey('trangthai.id'), nullable=False)
    uid = Column(String(20), ForeignKey('UID.uid'), nullable=False) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )