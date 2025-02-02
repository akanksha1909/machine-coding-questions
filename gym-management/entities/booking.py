import uuid

class Booking:
    def __init__(self, user, center, slot, day):
        self.id = str(uuid.uuid4())
        self.user = user
        self.center = center
        self.slot = slot
        self.day = day
