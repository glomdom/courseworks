# REJECT DYNAMIC TYPES EMBRACE TYPE SAFETY 🤠🤠🤠🤠🤠🤠🤠🤠

from typing import Generator

def even_numbers(number: int) -> Generator[int, None, None]:
    for num in range(2, number + 1, 2):
        yield num

def fibonacci(number: int) -> Generator[int, None, None]:
    a, b = 0, 1

    for _ in range(number):
        yield a

        a, b = b, a + b

for number in even_numbers(10):
    print(number)

print("")

for number in fibonacci(5):
    print(number)
