class EvenNumbers:
    def __init__(self, start, end):
        self.start = start if start % 2 == 0 else start + 1
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        even_number = self.current
        self.current += 2

        return even_number

class FibonacciIterator:
    def __init__(self, count):
        self.count = count
        self.n1, self.n2 = 0, 1
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.count:
            raise StopIteration

        if self.index == 0:
            self.index += 1

            return 0
        elif self.index == 1:
            self.index += 1

            return 1

        fib_number = self.n1 + self.n2
        self.n1, self.n2 = self.n2, fib_number
        self.index += 1

        return fib_number

print("even:")
even_numbers = EvenNumbers(3, 10)
for num in even_numbers:
    print(num)

print()
print("fib:")
fib_numbers = FibonacciIterator(10)
for num in fib_numbers:
    print(num)
