
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship


class Permission(Base):
    """
    Database model for permission
    """
    __tablename__ = "permissions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    users = relationship("UserPermission", back_populates="permission")
    roles = relationship("RolePermission", back_populates="permission") 