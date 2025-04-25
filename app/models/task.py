
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, func
from sqlalchemy.orm import relationship


class Task(Base):
    """
    Database model for task
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    individual_units = relationship("IndividualUnit", back_populates="task")
    unit_groups = relationship("UnitGroup", back_populates="task") 