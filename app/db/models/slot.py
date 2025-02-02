# app/db/models/slot.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base  # Ensure that the Base class is properly imported

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    slot_number = Column(String, unique=True, nullable=False)
    is_available = Column(Boolean, default=True, nullable=False)
    lot_id = Column(Integer, ForeignKey("parking_lots.id"), nullable=False)

    lot = relationship("ParkingLot", back_populates="slots")
