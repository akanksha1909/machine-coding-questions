from entities.user import User

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, name, email, phone, password):
        user = User(name, email, phone, password)
        self.users[user.id] = user
        return user.id
    
    def get_user(self, id):
        return self.users[id]