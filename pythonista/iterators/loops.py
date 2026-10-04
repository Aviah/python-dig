
SENTINEL_DEMO = 'foo'

class SimpleIterator:
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


for i in SimpleIterator(5):
    print(i)

print("-----")
i = SimpleIterator(3)
# "while itr" will not work: itr is an iterator *object*, so it will not normally evaluate to False
while True:
    try:
        print(next(i))
    except StopIteration:
        print("Done!")
        break


print("-----")
class CustomIterator:
    def __init__(self):
        self.itr = SimpleIterator(5, sentinel=SENTINEL_DEMO)

    def __call__(self):
        element = next(self.itr)
        if element != SENTINEL_DEMO:
            element = element * 100
        return element


# "iter" supports any callable, in the format iter(callable, sentinel). Will call it until the sentinel is returned
# It Enables iteration over objects that don't support __iter__ on their own
for x in iter(CustomIterator(), SENTINEL_DEMO):
    print(x)

print("-----")
itr = iter(CustomIterator(), SENTINEL_DEMO)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

try:
    next(itr)
except StopIteration:
    print("Iterator exhausted")
