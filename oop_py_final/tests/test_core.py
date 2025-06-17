import unittest
from unittest.mock import patch

from core.menu import Menu
from core.users import Admin, User
from core.decorators import time_tracker

class TestSystem(unittest.TestCase):
    def setUp(self) -> None:
        self.menu = Menu()

    def test_polymorphism(self) -> None:
        admin = Admin("admin", "123")
        user = User("user", "123")
        self.assertEqual(admin.access_level(), "admin")
        self.assertEqual(user.access_level(), "user")

    @patch("core.menu.time.sleep", return_value=None)
    def test_notify_execution_time(self, _) -> None:
        self.menu.logged_user = Admin("admin", "123")
        self.menu.notify("test")

    def test_delete_user(self) -> None:
        self.menu.users.append(User("user2", "123"))
        self.menu.logged_user = Admin("admin", "123")
        self.menu.delete_user("user2")
        self.assertFalse(any(u.username == "user2" for u in self.menu.users))

    def test_variable_arguments(self) -> None:
        self.menu.log_multiple_actions("act1", "act2", "act3")

if __name__ == "__main__":
    unittest.main()
