from abc import ABC, abstractmethod

class BaseUser(ABC):
    _id_counter = 1

    def __init__(self, username: str, password: str) -> None:
        self.id = BaseUser._id_counter
        BaseUser._id_counter += 1

        self.username = username
        self.password = password

    @abstractmethod
    def access_level(self) -> str:
        pass

class User(BaseUser):
    def access_level(self) -> str:
        return "user"

class Admin(BaseUser):
    def access_level(self) -> str:
        return "admin"
