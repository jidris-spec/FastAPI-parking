from sqlalchemy.orm import Session
from app.db.models.slot import Slot

class SlotRepository:
    def _init_(self, db: Session):
        self.db = db

    def create_slot(self, name: str, description: str, price: int, location: str) -> Slot:
        slot = Slot(name=name, description=description, price=price, location=location)
        self.db.add(slot)
        self.db.commit()
        self.db.refresh(slot)
        return slot



    def get_slot_by_id(self, slot_id: int) -> Slot:
        return self.db.query(Slot).filter(Slot.id == slot_id).first()
    
    def get_all_slots(self):
        return self.db.query(Slot).all()