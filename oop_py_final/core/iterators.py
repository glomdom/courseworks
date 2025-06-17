from core.users import BaseUser

class EvenIDIterator:
    def __init__(self, users: list[BaseUser]) -> None:
        self.users = [u for u in users if u.id % 2 == 0]
        self.index = 0

    def __iter__(self) -> 'EvenIDIterator':
        return self

    def __next__(self) -> BaseUser:
        if self.index >= len(self.users):
            raise StopIteration

        user = self.users[self.index]
        self.index += 1

        return user
