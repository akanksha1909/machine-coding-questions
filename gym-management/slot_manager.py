from entities.slot import Slot
from entities.center import Center

class SlotManager:
    def __init__(self):
        self.slots = {}
    
    def add_slot(self, center, slot_id, time, workout_type, capacity):
        slot = Slot(slot_id, center.id, time, workout_type, capacity)
        center.add_slot(slot)