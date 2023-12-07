import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class user_has_permissions(Base):
    """
    Database model for an uid
    """
    __tablename__ = 'user_has_permissions'
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    permission_id = Column(Integer, ForeignKey('permission.id'), nullable=False) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    permissions = relationship("user", back_populates="Permission")