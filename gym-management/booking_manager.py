from entities.booking import Booking

class BookingManager:
    def __init__(self):
        self.bookings = {}

    def book_workout(self, user, center, slot, day):
        if not user or not center or not slot or not day:
            print("Invalid data")
            return
        
        for booking in self.bookings.values():
            if (
                booking.user.user_id == user.user_id
                and booking.center.center_id == center.center_id
                and booking.slot.slot_id == slot.slot_id
                and booking.day == day
            ):
                print("User has already booked this slot.")
                return
            
        if slot.is_available():
            booking = Booking(user, center, slot, day)
            if slot.book_slot():
                self.bookings[booking.id] = booking
                return booking
            else:
                print("Failed to book slot")
        else:
            print("Slot is already full")

