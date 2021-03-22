import datetime


class User:

    def __init__(self, name: str):
        self.name = name
        self.added_at = datetime.datetime.now()


class Users:

    def __init__(self):
        self.users = []

    def add_user(self, user: User):
        self.users.append(user)

    def get_user_by_name(self, name: str):
        return list(filter(lambda x: x.name == name, self.users))


USERS = Users()
