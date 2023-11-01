import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class user_donvi(Base):
    """
    Database model for an user_donvi table
    """

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    donvi_id = Column(Integer, ForeignKey('donvi.id'), nullable=False) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    user = relationship("donvi", back_populates="user")