class Slot:
    def __init__(self, id, center_id, time, workout_type, capacity):
        self.id = id
        self.center_id = center_id
        self.time = time
        self.workout_type = workout_type
        self.capacity = capacity
        self.bookings = 0

    def is_available(self):
        return self.capacity - self.bookings
    
    def book_slot(self):
        if self.is_available():
            self.bookings += 1
            return True
        return False