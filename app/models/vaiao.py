import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class vaiao(Base):
    """
    Database model for an uid
    """
    __tablename__="vaiao"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    uid_hoinhom = Column(String(20), nullable=False)
    uid_vaiao = Column(String(20), nullable=False) 
    active = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )