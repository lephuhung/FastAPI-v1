from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Report(Base):
    """
    Database model for report
    """
    __tablename__ = "reports"
    id = Column(Integer, primary_key=True, index=True)
    social_account_uid = Column(String(255), index=True)
    content_note = Column(String(1000))
    comment = Column(String(1000))
    action = Column(String(1000))
    related_social_account_uid = Column(String(255))
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    # social_account = relationship("SocialAccount", back_populates="reports")
    user = relationship("User", back_populates="reports") 