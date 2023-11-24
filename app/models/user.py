import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class User(Base):
    """
    Database model for an uid
    """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(255),nullable=False)
    password = Column(String(255),nullable=False) 
    salt = Column(String(20), nullable=False)
    active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(
        DateTime,
        default=datetime.datetime.now(),
        onupdate=datetime.datetime.now(),
    )