from center_manager import CenterManager
from slot_manager import SlotManager
from user_manager import UserManager
from booking_manager import BookingManager

class FlipFitSystem:
    def __init__(self):
        self.center_manager = CenterManager()
        self.slot_manager = SlotManager()
        self.user_manager = UserManager()
        self.booking_manager = BookingManager(self.user_manager, self.center_manager)
    
    def add_center(self, center_id, name):
        self.center_manager.add_center(center_id, name)

    def add_slot(self, center_id, slot_id, time, workout_type, capacity):
        center = self.center_manager.get_center(center_id)
        if not center:
            print("Center not found!")
            return
        self.slot_manager.add_slot(center, slot_id, time, workout_type, capacity)

    def register_user(self, name, email, phone, password):
        return self.user_manager.register_user(name, email, phone, password)
    
    def view_workouts_for_day(self, day):
        for center in self.center_manager.centers.values():
            slots = center.get_slots_for_day()
            if not slots:
                print(f"No slots available for center {center.name}")
                continue
        
            for slot in slots.values():
                print(f"Center ID: {center.id}, Center Name: {center.name}, {slot.capacity}")

    def book_workout(self, user_id, center_id, slot_id, day):
        booking = self.booking_manager.book_workout(user_id, center_id, slot_id, day)
        if booking:
            print(f"Booking successful: {booking}")
        else:
            print("Failed to book workout.")

    def view_user_plan(self, user_id, day):
        bookings = self.booking_manager.get_user_bookings(user_id, day)
        if not bookings:
            print("No bookings found for this user on the specified day.")
            return
    
        for booking in bookings:
            print(f"User booking plan for a day {booking}")


    def get_center(self, center_id):
        return self.center_manager.get_center(center_id)


    