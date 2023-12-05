import datetime
from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey, Nullable
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class role_has_permission(Base):
    """
    Database model for an uid
    """

    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    role_id = Column(Integer, ForeignKey('role.id'), nullable=False)
    permission_id = Column(String(20), ForeignKey('permission.uid'), nullable=False) 
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    permission = relationship("role", back_populates="permission")