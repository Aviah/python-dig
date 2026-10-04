class SimpleIterator:
    def __init__(self, times: int):
        self.itr = 0
        self.times = times

    def __iter__(self):
        # An iterator implements __iter__ and returns itself.
        return self

    def __next__(self):
        if self.itr < self.times:
            self.itr += 1
            return self.itr

        raise StopIteration


for i in SimpleIterator(5):
    print(i)

print("-----")
itr = map(lambda x: x * 100, SimpleIterator(10))
print(itr)
print(next(itr))
print(next(itr))
print(list(itr))


print("-----")

itr = SimpleIterator(4)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
try:
    print(next(itr))
except StopIteration:
    print("Exhausted")


print("-----")

m = SimpleIterator(3)
n = iter(SimpleIterator(3))
print([x for x in m])
print([x for x in n])
print(list(iter(iter(iter(SimpleIterator(4))))))

print("-----")
itr1 = SimpleIterator(10)
next(itr1)
next(itr1)
itr2 = iter(itr1)
print(next(itr2))
print(next(itr1))
print(next(itr2))
assert itr1 is itr2

