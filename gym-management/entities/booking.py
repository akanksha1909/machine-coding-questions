import uuid

class Booking:
    def __init__(self, user_id, center_id, slot_id, day):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.center_id = center_id
        self.slot_id = slot_id
        self.day = day
