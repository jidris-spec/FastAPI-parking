# app/db/models/parking_lot.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.base import Base  # Ensure that Base is imported

class ParkingLot(Base):
    __tablename__ = "parking_lots"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  # You can add more fields if needed

    # Relationship with the Slot model
    slots = relationship("Slot", back_populates="lot")
