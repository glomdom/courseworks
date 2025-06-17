from core.users import Admin, User
from core.decorators import time_tracker, require_admin
from core.iterators import EvenIDIterator

import time

class Menu:
    def __init__(self) -> None:
        self.users: list[User | Admin] = []
        self.logged_user: User | Admin | None = None

    def run(self) -> None:
        self.users.append(Admin("admin", "adminpass"))
        self.users.append(User("user1", "pass1"))
        self.users.append(User("user2", "pass2"))
        self.users.append(User("user3", "pass3"))
        self.users.append(User("user4", "pass4"))
        self.users.append(User("user5", "pass5"))
        self.users.append(User("user6", "pass6"))

        self.login("admin", "adminpass")
        self.log_multiple_actions("login", "access_dashboard", "delete_user")
        self.notify("System update at 8PM")
        self.delete_user("user1")

        print("Users with even IDs:")
        for user in EvenIDIterator(self.users):
            print(f" - {user.username} (ID: {user.id})")

    def login(self, username: str, password: str) -> None:
        for user in self.users:
            if user.username == username and user.password == password:
                self.logged_user = user

                break

    @time_tracker
    def notify(self, message: str) -> None:
        time.sleep(0.1)

        print(f"Notification: {message}")

    @require_admin
    def delete_user(self, username: str) -> None:
        self.users = [user for user in self.users if user.username != username]

        print(f"User '{username}' deleted")

    def log_multiple_actions(self, *actions: str) -> None:
        for action in actions:
            print(f"Action logged: {action}")
