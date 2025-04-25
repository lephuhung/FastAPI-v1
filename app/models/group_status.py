
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship


class GroupStatus(Base):
    """
    Database model for group status
    """
    __tablename__ = "group_statuses"
    id = Column(Integer, primary_key=True, index=True)
    status_id = Column(Integer, ForeignKey("statuses.id"))
    social_account_uid = Column(String(255), ForeignKey("social_accounts.uid"), index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    status = relationship("Status", back_populates="group_statuses")
    social_account = relationship("SocialAccount", back_populates="group_statuses") 