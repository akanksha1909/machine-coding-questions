class Center:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.slots = {}

    def add_slot(self, slot):
        self.slots[slot.id] = slot

    def get_slots_for_day(self):
        return self.slots
    
    def get_slot_by_id(self, slot_id):
        return self.slots[slot_id]