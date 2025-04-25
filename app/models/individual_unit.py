
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class IndividualUnit(Base):
    """
    Database model for individual unit relationship
    """
    __tablename__ = "individual_units"
    id = Column(Integer, primary_key=True, index=True)
    unit_id = Column(UUID(as_uuid=True), ForeignKey("units.id"), index=True)
    individual_id = Column(UUID(as_uuid=True), ForeignKey("individuals.id"), index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    unit = relationship("Unit", back_populates="individuals")
    individual = relationship("Individual", back_populates="units")
    task = relationship("Task", back_populates="individual_units") 