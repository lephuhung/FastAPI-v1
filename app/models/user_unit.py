from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from app.db.base_class import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class UserUnit(Base):
    """
    Database model for user_unit
    """
    __tablename__ = "user_units"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.id", ondelete="RESTRICT"), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="units")
    unit = relationship("Unit", back_populates="users") 