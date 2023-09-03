class Iterator:
    def __init__(self, times: int):
        self.itr = 0
        self.times = times

    def __iter__(self):
        # An iterator should support __iter__, like an iterable, and return self
        return self

    def __next__(self):
        if self.itr < self.times:
            self.itr += 1
            return self.itr

        raise StopIteration


for i in Iterator(5):
    print(i)


print(list(map(lambda x: x * 100, iter(Iterator(10)))))

iterator = Iterator(4)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    print(next(iterator))
except StopIteration:
    print("Exhausted")


m = Iterator(3)
n = iter(Iterator(3))
print([x for x in m])
print([x for x in n])
