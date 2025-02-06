from sqlalchemy.orm import Session
from app.db.repositories.booking_repository import BookingRepository
from app.schemas.booking import BookingCreate, BookingUpdate, BookingResponse
from app.services.user_service import UserService
from app.services.slot_service import SlotService

class BookingService:
    def __init__(self, db: Session):
        self.booking_repository = BookingRepository(db)
        self.user_service = UserService(db)
        self.slot_service = SlotService(db)
# create a new booking.
    def create_booking(self, booking_data: BookingCreate):
    #    check if user and slot exists
        slot = self.slot_service.get_slot_by_id(booking_data.slot_id)
        if not slot:
            raise ValueError("slot not found")
        
        user = self.user_service.get_user_by_id(booking_data.user_id)
        if not user:
            raise ValueError("user not found")
    
        booking = self.booking_repository.create_booking(
            user_id=booking_data.user_id,
            slot_id=booking_data.slot_id,
            price=booking_data.price,
        ) 
        # update slot if booking is successful
        slot.is_available =  False
        self.slot_service.update_slot(slot.id, slot)
        return booking      
    
    def get_booking_by_id(self, booking_id: int):
            booking = self.booking_repository.get_booking_by_id(booking_id)
            if not booking:
                raise ValueError("booking not found")
            return booking
    
    # def update_booking(self, booking_id: int, booking_data: BookingUpdate):
    #     booking = self.booking_repository.get_booking_by_id(booking_id)
    #     booking = self.booking_repository.update_booking(
    #         price=booking_data.price,
    #         slot_id=booking_data.slot_id,
    #         status=booking_data.status
    #     )
    def update_booking(self, booking_id: int, booking_data: BookingUpdate):
        # Pass the booking_id as the first argument
        booking = self.booking_repository.update_booking(
            booking_id=booking_id,  # Pass the booking_id here
            price=booking_data.price,
            slot_id=booking_data.slot_id,
            status=booking_data.status
        )
        return booking
        return booking
    def get_all_bookings(self):
        bookings = self.booking_repository.get_all_bookings()
        return bookings
    