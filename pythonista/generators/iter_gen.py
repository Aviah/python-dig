class GeneratorBasedIterable:
    """
    generator-backed iterable
    """
    def __init__(self, start, end):
        self._start, self._end = start, end

    def __iter__(self):
        crr = self._start
        while crr < self._end:
            yield crr
            crr += 1


g = GeneratorBasedIterable(100, 105)
i = iter(g)
print(list(i))
print(list(i))
try:
    next(i)
except StopIteration as e:
    print(repr(e))