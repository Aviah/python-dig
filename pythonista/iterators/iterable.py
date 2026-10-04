class SimpleIterator:
    def __init__(self, times: int):
        self.itr = 0
        self.times = times

    def __iter__(self):
        return self

    def __next__(self):
        if self.itr < self.times:
            self.itr += 1
            return self.itr

        raise StopIteration


class SimpleIterable:
    # Iterable is the factory of iterators
    def __init__(self, times: int):
        self.times = times

    def __iter__(self):
        return SimpleIterator(self.times)  # return a fresh iterator


itb = SimpleIterable(3)
print([x for x in itb])  # exhausted
print([x for x in itb])  # fresh iterator
