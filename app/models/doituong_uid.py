from uuid import uuid4

from app.db.base_class import Base
from sqlalchemy import Boolean, Column, DateTime, String, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship


class Individual_UID(Base):
    """
    Database model for an Individual UUID
    """
    __tablename__="individual_uid"
    id = Column(Integer, primary_key=True, index=True, nullable=False, autoincrement=True)
    individual_id = Column(Integer, ForeignKey("individual.id"))
    uid = Column(String(20), ForeignKey("uid.uid") )
    relationship_id= Column(Integer, ForeignKey("relationship.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(
        DateTime,
        default=func.now(),
        onupdate=func.now(),
    )