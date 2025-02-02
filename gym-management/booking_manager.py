from entities.booking import Booking
class BookingManager:
    def __init__(self, user_manager, center_manager):
        self.bookings = {}
        self.center_manager = center_manager
        self.user_manager = user_manager

    def book_workout(self, user_id, center_id, slot_id, day):
        if not user_id or not center_id or not slot_id or not day:
            print("Invalid data")
            return
        
        user = self.user_manager.get_user(user_id)
        center = self.center_manager.get_center(center_id) 
        slot = center.get_slot_by_id(slot_id)
        for booking in self.bookings.values():
            if (
                booking.user_id == user.id
                and booking.center_id == center.id
                and booking.slot_id == slot.id
                and booking.day == day
            ):
                print("User has already booked this slot.")
                return

        if slot.is_available():
            booking = Booking(user_id, center_id, slot_id, day)
            if slot.book_slot():
                self.bookings[booking.id] = booking
                print("Booking Successful!")
                return booking
            else:
                print("Failed to book slot")
        else:
            print("Slot is already full")

