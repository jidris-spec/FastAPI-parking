# app/services/user_service.py
from sqlalchemy.orm import Session
from app.db.repositories.slot_repository import SlotRepository
from app.schemas.slot import SlotCreate, SlotUpdate,SlotResponse
from app.utils.email import send_email

class SlotService:
    def __init__(self, db: Session):
        self.slot_repository = SlotRepository(db)

    def create_slot(self, slot_data: SlotCreate):
        existing_slot = self.slot_repository.get_slot_by_id(slot_data.id)
        if existing_slot:
            raise ValueError("slot with this id already exists")
        
        slot = self.slot_repository.create_slot(
            id=slot_data.id,
            name=slot_data.name,
            location=slot_data.location,
            is_available=slot_data.is_available,
        )
        return slot

        
    def get_slot_by_id(self, slot_id: int):
            slot = self.slot_repository.get_slot_by_id(slot_id)
            if not slot:
                raise ValueError("slot not found")
            return slot

    