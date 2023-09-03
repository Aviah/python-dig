class Iterator:
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


class Iterable:
    def __init__(self, times: int):
        self.times = times

    def __iter__(self):
        return Iterator(self.times)  # return a fresh iterator


i = Iterable(3)
print([x for x in i])  # exhausted
print([x for x in i])  # yet iterable again
