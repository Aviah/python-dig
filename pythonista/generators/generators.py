import itertools

g = (x for x in range(4))
print(g)
print(next(g))
print(next(g))
print([x for x in g])

print(sum(x for x in range(100)))  # no need for [...]

g = (x for x in itertools.cycle(('foo', 'baz', 'bar')))
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # cycle, infinite generator


def simple_gen():
    yield 'foo'
    yield 'baz'
    yield 'spam'


g = simple_gen()
print(next(g))
print(next(g))
print(next(g))


def gen(seq):
    for element in seq:
        yield seq
    print("meh")


g = gen(['foo', 'baz', 'bar'])
print(next(g))
print(next(g))
print(next(g))
print("=====")
try:
    print(next(g))
except StopIteration as e:
    print(repr(e))

print([x for x in g])

sentinel = object()
assert next(g, sentinel) is sentinel  # verify if a generator is empty w/o StopIteration


def incr_gen(n):
    x = 0
    while x < n:
        yield x
        x += 1


g = incr_gen(8)
print(g)
print([x for x in g])


def infinite_gen():
    answer = 42
    print(f"Found the answer")
    while True:
        yield answer


for idx, element in enumerate(infinite_gen()):
    print(idx, element)
    if idx > 3:
        break  # otherwise infinite
