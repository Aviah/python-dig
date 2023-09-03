m = ['foo', 'baz', 'spam', 'eggs']

i = iter(m)
print(i)
print(next(i))
print([x for x in i])  # continue from last next
print([x for x in i])  # works, exhausted so empty
try:
    next(i)
except StopIteration as e:
    print(repr(e))

print("=====")
itr = iter(['foo', 'baz', 'spam'])
# while itr:  will not work. itr is an iterator object, and will always evaluate to True, even when stopped
while True:
    try:
        print(next(itr))
    except StopIteration as e:
        print(repr(e))
        break

print("=====")

i = iter(['foo', 'baz', 'spam'])
print(next(i))
print(next(i))
print(next(i))
sentinel = object()
print(next(i, sentinel))
assert next(i, sentinel) is sentinel  # exhausted, w/o raising StopIteration

print("=====")
# create multiple iterators
import itertools

i1, i2 = itertools.tee(m, 2)
print([x for x in i1])
print([x for x in i2])  # an easy way to re-use the iterator

print("=====")
# create iterator from any callable, even if the object is not an iterator
from functools import partial


def gen(seq):
    for element in seq:
        yield element


def call_gen(g):
    return next(g)


itr = iter(partial(call_gen, gen(m)), 'spam')
print([x for x in itr])  # stops at sentinel value 'spam'

print("=====")
# infinite iterator
import itertools

for idx, element in enumerate(itertools.cycle([100, 200, 300])):
    print(idx, element)
    if idx > 5:
        break  # otherwise inifinte iterator


print("=====")
# filter
for w in itertools.filterfalse(lambda x: len(x) == 3, ["All", "generalizations", "are", "false"]):
    print(w)


print("=====")


# args
def f(*args):
    print(args)


itr = iter(['foo', 'baz', 'bar'])
f(itr)
f(*itr)
