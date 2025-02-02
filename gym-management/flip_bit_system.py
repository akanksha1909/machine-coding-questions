from center_manager import CenterManager
from slot_manager import SlotManager
from user_manager import UserManager
from booking_manager import BookingManager

class FlipFitSystem:
    def __init__(self):
        self.center_manager = CenterManager()
        self.slot_manager = SlotManager()
        self.user_manager = UserManager()
        self.booking_manager = BookingManager()
    
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
            for slot in center.get_slots_for_day().values():
                print(f"Center ID: {center.id}, Center Name: {center.name}, {slot.capacity}")

    def book_workout(self, user_id, center_id, slot_id, day):
        user = self.user_manager.get_user(user_id)
        center = self.center_manager.get_center(center_id)
        slot = center.get_slot_by_id(slot_id)
        self.booking_manager.book_workout(user, center, slot, day)

    def view_user_plan(self, user_id, day):
        plans = []
        for booking in self.booking_manager.bookings.values():
            if booking.user.id == user_id and booking.day == day:
                plans.append(booking)

        for plan in plans:
            print(f"User booking plan for a day {plan}")


    def get_center(self, center_id):
        return self.center_manager.get_center(center_id)


    