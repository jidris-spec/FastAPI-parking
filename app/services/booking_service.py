from app.db.repositories.booking_repository import BookingRepository
from app.db.models.booking import Booking
from sqlalchemy.orm import Session
from typing import List, Optional

class BookingService:
    def __init__(self, db: Session):
        self.db = db
        self.booking_repository = BookingRepository(db)

    def create_booking(self, user_id: int, slot_id: int, price: int) -> Booking:
        """ 
        create a new booking.
        """
        return self.booking_repository.create_booking(user_id, slot_id, price)
    
    def update_booking(self, booking_id: int, price: Optional[int] = None, slot_id: Optional[int] = None) -> Optional[Booking]:
        """
        update existing booking by booking id 
        """
        return self.booking_repository.update_booking(booking_id, price,slot_id)
    
    def get_booking_by_id(self, booking_id:int) -> Optional [Booking]:
        """
        Retrieve a booking by booking id.
        """
        return self.booking_repository.get_booking_by_id(booking_id)
    def get_all_bookings(self) -> List[Booking]:
        """
        Retrieve all bookings.

        """
        return self.booking_repository.get_all_bookings()
    