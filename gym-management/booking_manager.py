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
        
        try:
            user = self.user_manager.get_user(user_id)
            center = self.center_manager.get_center(center_id)
            slot = center.get_slot_by_id(slot_id)
        except KeyError as e:
            print(f"Error: {str(e)}")
            return

        for booking in self.bookings.values():
            if (
                booking.user_id == user.id
                and booking.center_id == center.id
                and booking.slot_id == slot.id
                and booking.day == day
            ):
                print("User has already booked this slot.")
                return

        if not slot.is_available():
            print("Slot is full!")
            return
        
        booking = Booking(user_id, center_id, slot_id, day)
        if slot.book_slot():
            self.bookings[booking.id] = booking
            return booking
        
    def get_user_bookings(self, user_id, day):
        bookings = []
        for booking in self.bookings.values():
            if booking.user_id == user_id and booking.day == day:
                bookings.append(booking)
        return bookings

