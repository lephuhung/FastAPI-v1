from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class User(Base):
    """
    Database model for user
    """
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=generate_uuid)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    salt = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    roles = relationship("UserRole", back_populates="user")
    permissions = relationship("UserPermission", back_populates="user")
    units = relationship("UserUnit", back_populates="user")
    reports = relationship("Report", back_populates="user")
