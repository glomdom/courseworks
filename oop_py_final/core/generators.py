from typing import Generator

def generate_even_grades(limit: int) -> Generator[int, None, None]:
    for grade in range(0, limit + 1, 2):
        yield grade

def generate_student_ids(start: int, end: int) -> Generator[int, None, None]:
    for sid in range(start, end + 1):
        yield sid
