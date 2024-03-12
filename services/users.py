from models.users import User


class UserService:
    users = []

    def __init__(self, user: User = None):
        self.user = user

    def add_users(self, user):
        """"""
        self.users.append(user)

    def get_users(self):
        return self.users
