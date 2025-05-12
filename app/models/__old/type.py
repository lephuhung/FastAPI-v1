from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer
from sqlalchemy.orm import relationship


class type(Base):
    """
    Database model for an uid
    """
    __tablename__='type'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True) 
    name = Column(String(255))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )