
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class UnitGroup(Base):
    """
    Database model for unit group relationship
    """
    __tablename__ = "unit_groups"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.id"), index=True)
    social_account_uid = Column(String(255), ForeignKey("social_accounts.uid"), index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    unit = relationship("Unit", back_populates="groups")
    social_account = relationship("SocialAccount", back_populates="unit_groups")
    task = relationship("Task", back_populates="unit_groups") 