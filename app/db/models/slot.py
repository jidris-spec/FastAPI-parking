
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base  # Ensure that the Base class is properly imported

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    is_available = Column(Boolean, default=True, nullable=False)
    address = Column(String, nullable=False)
    price_per_hour = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey("users.id"))
    slot_capacity = Column(Integer, nullable=False)
    slot_tag = Column(String, nullable=False, unique=True)