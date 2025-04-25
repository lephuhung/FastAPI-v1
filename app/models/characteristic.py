
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String,Integer, func
from sqlalchemy.orm import relationship


class Characteristic(Base):
    """
    Database model for characteristic
    """
    __tablename__ = "characteristics"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    color = Column(String(7))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    group_characteristics = relationship("GroupCharacteristic", back_populates="characteristic") 