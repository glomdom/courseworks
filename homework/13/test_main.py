import unittest

from unittest.mock import patch
from main import show_menu, say_hello, add_numbers, multiply_numbers, menu_choice

class TestMenuSystem(unittest.TestCase):
    def test_show_menu(self):
        expected_menu = """1. Say 'Hello'.
2. Add numbers.
3. Exit."""

        self.assertEqual(show_menu(), expected_menu)
    
    def test_say_hello(self):
        self.assertEqual(say_hello(), "Hello, User!")
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 5), 7)
    
    @patch('main.say_hello')
    def test_menu_choice_calls_say_hello(self, mock_say_hello):
        mock_say_hello.return_value = "Hello, User!"

        result = menu_choice(1)
        mock_say_hello.assert_called_once()
        self.assertEqual(result, "Hello, User!")
    
    @patch('main.add_numbers')
    def test_menu_choice_calls_add_numbers(self, mock_add_numbers):
        mock_add_numbers.return_value = 10

        result = menu_choice(2)
        mock_add_numbers.assert_called_once_with(3, 4)
        self.assertEqual(result, 10)
    
    def test_menu_choice_exiting(self):
        self.assertEqual(menu_choice(3), "Exiting...")
    
    def test_menu_choice_invalid(self):
        self.assertEqual(menu_choice(99), "Invalid Choice!")
    
    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 4), 12)
        self.assertEqual(multiply_numbers(-2, 5), -10)
        self.assertEqual(multiply_numbers(0, 10), 0)

if __name__ == '__main__':
    unittest.main()
