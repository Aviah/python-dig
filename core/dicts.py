
from collections import ChainMap, defaultdict
from functools import partial
from random import randint


colors = {
    'red': 1,
    'blue': 'favourite',
    'orange': 'maybe',
    (1, 2, 3): 4,
    (5, 6, 7): [8, 9, "10"],
}


print(colors.keys())
print(colors.values())
print(list(colors.keys()))
print(list(colors.values()))
c = colors.keys()
del colors['red']
print('red' in c)
print(type(c))
print(list(zip(colors.keys(), colors.values())))  # keys, values are iterators
for k in colors:
    print(k)
d1 = dict(c=3, a=1, b=2)
print(d1)
print(type(d1.items().mapping))  # read only proxy
print(type(d1.keys().mapping))
print(type(d1.values().mapping))
s = set(['a', 'b', 'x'])
print(s.difference(d1.items().mapping))
assert set([100, 200, 300]).isdisjoint(d1.values().mapping)
print(d1.pop('a'))
del d1['b']
print(d1)


assert not d1.values().mapping.__contains__(4)
print(d1.keys().mapping.__iter__())

# comprehension
print("=====")
d = {k: v for k, v in [('foo', 'bar'), ('spam', 'eggs')]}
print(d)
foo = {'a': 1, 'b': 2}
baz = {'abc': 100, 'def': 200}
print({**foo, **baz})
print(dict(**baz, **foo))  # note the order


print("=====")
# https://www.youtube.com/watch?v=oMyy4Sm0uBs
# order of insertion
d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
e = {'ircd': 6667, 'zope': 9673, 'smtp': 21, 'dict': 2628, 'svn': 3690}
print(d)
print(e)
print(d == e)

d1 = dict(**d)
assert d1 == d
assert d1 is not d
e1 = dict(**e)
for i in range(5):
    # pop item by order (note: popitem is thread safe)
    print(d1.popitem())
    print(e1.popitem())

print("=====")
d.update(e)
print(d)
e['ircd'] = 5555
d.update(e)
print(d)


# see hashing_eq.py
try:
    lst = [1, 2, 3]
    d[lst] = "maybe"
except Exception as e:
    print(repr(e))

d[(1, 2, 3)] = 'jump'
print(d[(1, 2, 3)])


print("=====")

d = defaultdict(list)
d['foo'].append(1)
d['baz'].extend([100, 200, 300])
print(d)


d = defaultdict(partial(randint, 0, 100))
print(d)
print(d['foo'])
print(d['baz'])
print(d)

d = {}
m = d.setdefault('spam', 'eggs')
print(d)
print(m)
n = d.setdefault('spam', 'baz')
print(d)
print(n)


try:
    d['foo']
except KeyError as e:
    print(repr(e))

assert d.get('foo') is None
print(d.get('foo', 'block'))

d = {'foo': 1, 'bump': 2}
print(d)
d.clear()
print(d)


print("\n===== ChainMap =====")
d = {'spam': 'eggs', 'bar': 'baz'}
e = {'foo': 'maybe'}
print(list(ChainMap(d, e).items()))
assert 'spam' in ChainMap(d, e)
assert 'foo' in ChainMap(d, e)


print("\n===== Iterate & mutate =====")
d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
for k in d:
    # mutate a value while iterating keys, works
    d['smtp'] = 9999
print(d)

from random import randint

for k in list(d.keys()):
    # iterate over a copy of the keys, works
    if k.startswith('s'):
        d[randint(0, 100000)] = 'random'
print(d)

for k in list(d.keys()):
    # iterate over a copy of the keys, works
    if type(k) == int:
        del d[k]
print(d)

# RuntimeError: dictionary changed size during iteration
d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
try:  # the try clause should enclose the loop over dict block
    for k in d:
        if k == 'smtp':
            d['foo'] = 'baz'  # iterate over a view of the dict, fails
except Exception as e:
    print(repr(e))

try:
    for k in d:
        del d[k]  # del key during an iteration over keys, fails
except Exception as e:
    print(repr(e))

