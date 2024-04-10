import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class quantrivien(Base):
    """
    Database model for an uid
    """
    __tablename__='quantrivien'
    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String(20), nullable=False)
    uid_facebook = Column(String(20), ForeignKey('uid.uid'), nullable=False) 
    moiquanhe_id = Column(String(20), ForeignKey('moiquanhe.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )