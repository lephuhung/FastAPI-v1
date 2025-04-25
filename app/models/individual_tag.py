
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class IndividualTag(Base):
    """
    Database model for individual tag relationship
    """
    __tablename__ = "individual_tags"
    id = Column(Integer, primary_key=True, index=True)
    individual_id = Column(UUID(as_uuid=True), ForeignKey("individuals.id"), index=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    individual = relationship("Individual", back_populates="tags")
    tag = relationship("Tag", back_populates="individuals") 