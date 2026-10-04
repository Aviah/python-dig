import itertools

mylist = ['foo', 'baz', 'spam', 'eggs']

print("===== Iterate until consumed =====")
i = iter(mylist)
print(i)
print(next(i))
print([x for x in i])  # continue from last next
print([x for x in i])  # works, exhausted so empty
try:
    next(i)
except StopIteration as e:
    print(repr(e))


print("-----")

i = iter(['foo', 'baz', 'spam', 'eggs'])
print(next(i))
print(next(i))
sentinel = object()
print(next(i, sentinel))
print(next(i, sentinel))
r = next(i, sentinel)
print(r)
assert r is sentinel  # exhausted, w/o raising StopIteration

print("\n===== Unpack =====")

def f(*args):
    print(args)

itr = iter(['foo', 'baz', 'bar'])
f(itr)
f(*itr)


print("\n===== Itertools =====")

print("----- create multiple iterators")
i1, i2 = itertools.tee(mylist, 2)
print([x for x in i1])
print([x for x in i2])  # tee provides multiple iterators from the same iterable


print("----- Infinite iterator")
for idx, element in enumerate(itertools.cycle([100, 200, 300])):
    print(idx, element)
    if idx > 5:
        break  # otherwise infinite iterator


print("----- Filter")
for w in itertools.filterfalse(lambda x: len(x) == 3, ["All", "generalizations", "are", "false"]):
    print(w)


