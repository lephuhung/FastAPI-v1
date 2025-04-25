from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Role_has_permission(Base):
    """
    Database model for an uid
    """
    __tablename__='role_has_permission'
    id = Column(Integer, primary_key=True, index=True,nullable=False, autoincrement=True)
    role_id = Column(UUID(as_uuid=True),ForeignKey("role.id"),primary_key=True,nullable=False)
    permission_id = Column(Integer, ForeignKey('permission.id'), nullable=False) 
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    # permission = relationship("role", back_populates="permission")