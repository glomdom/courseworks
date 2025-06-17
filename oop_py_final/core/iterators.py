class EvenIDIterator:
    def __init__(self, ids: list[int]) -> None:
        self.ids = [i for i in ids if i % 2 == 0]
        self.index = 0

    def __iter__(self) -> 'EvenIDIterator':
        return self

    def __next__(self) -> int:
        if self.index >= len(self.ids):
            raise StopIteration
        
        value = self.ids[self.index]
        self.index += 1

        return value
