
from app.db.base_class import Base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship


class GroupCharacteristic(Base):
    """
    Database model for group characteristic
    """
    __tablename__ = "group_characteristics"
    id = Column(Integer, primary_key=True, index=True)
    characteristic_id = Column(Integer, ForeignKey("characteristics.id"))
    social_account_uid = Column(String(255), ForeignKey("social_accounts.uid"), index=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )
    
    # Relationships
    characteristic = relationship("Characteristic", back_populates="group_characteristics")
    social_account = relationship("SocialAccount", back_populates="group_characteristics") 