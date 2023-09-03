class Iterator:
    def __init__(self, times: int, sentinel=None):
        self.itr = 0
        self.times = times
        self.sentinel = sentinel

    def __iter__(self):
        return self

    def __next__(self):
        if self.itr < self.times:
            self.itr += 1
            return self.itr
        elif self.sentinel is not None:
            _sentinel = self.sentinel
            self.sentinel = None
            return _sentinel

        raise StopIteration


for i in Iterator(5):
    print(i)


i = Iterator(3)
while True:
    try:
        print(next(i))
    except StopIteration:
        print("Done!")
        break


SENTINEL = 'foo'


class CustomIterator:
    def __init__(self):
        self.itr = Iterator(5, sentinel=SENTINEL)

    def __call__(self):
        element = next(self.itr)
        if element != SENTINEL:
            element = element * 100
        return element


# Enable iteration over objects that don't support the iter protocol
for x in iter(CustomIterator(), SENTINEL):
    print(x)
