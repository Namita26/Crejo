from utils.exception import CrejoException
from user.model import User, USERS
from typing import List


class UserService:

    @staticmethod
    def add_user(name: str) -> User:
        if not name or type(name) != str:
            raise CrejoException("E100", "Invalid Name")
        user = User(name)
        USERS.add_user(user)

    @staticmethod
    def get_users() -> List[User]:
        for x in USERS.users:
            print(x.name)
        return USERS.users

    @staticmethod
    def get_user_by_name(name: str) -> User:
        return USERS.get_user_by_name(name)
