def show_menu():
    return """1. Say 'Hello'.
2. Add numbers.
3. Exit."""

def say_hello():
    return "Hello, User!"

def add_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b

def menu_choice(choice):
    if choice == 1:
        return say_hello()
    elif choice == 2:
        return add_numbers(3, 4) # example values
    elif choice == 3:
        return "Exiting..."
    else:
        return "Invalid Choice!"
