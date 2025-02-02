from entities.center import Center

class CenterManager:
    def __init__(self):
        self.centers = {}
    
    def add_center(self, id, name):
        center = Center(id, name)
        self.centers[id] = center

    def get_center(self, id):
        return self.centers[id]
