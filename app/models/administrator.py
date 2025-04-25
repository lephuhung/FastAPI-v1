
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey,func
from sqlalchemy.orm import relationship


class Administrator(Base):
    """
    Database model for administrator
    """
    __tablename__ = "administrators"
    id = Column(Integer, primary_key=True, index=True)
    facebook_uid = Column(String(255), unique=True, index=True)
    uid = Column(String(255))
    relationship_id = Column(Integer, ForeignKey("relationships.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    relationship = relationship("Relationship", back_populates="administrators") 