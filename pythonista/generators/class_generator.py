class Generator:
    def __init__(self, start, end):
        self._start, self._end = start, end

    def __iter__(self):
        self._crr = self._start
        while self._crr < self._end:
            yield self._crr
            self._crr += 1


g = Generator(100, 105)
i = iter(g)
print(list(i))
print(list(i))
try:
    next(i)
except StopIteration as e:
    print(repr(e))
    print(g._crr)
