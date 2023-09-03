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

print("=====")
from collections import ChainMap, defaultdict
from random import randint

d = defaultdict(list)
d['foo'].append(1)
d['baz'].extend([100, 200, 300])
print(d)


from functools import partial

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


print("=====")
d = {'spam': 'eggs', 'bar': 'baz'}
e = {'foo': 'maybe'}
print(list(ChainMap(d, e).items()))
assert 'spam' in ChainMap(d, e)
assert 'foo' in ChainMap(d, e)


print("=====")


class AClass:
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.y == other.y


class BClass(AClass):
    def __hash__(self):
        # When defining custom __eq__, Python sets __hash__ to None, even if parent class *has* __hash__
        # To enable hashing, have to explicitly define it
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x


a1 = AClass(123, 'foo')
a2 = AClass(123, 'baz')
d = {a1: 100}
print(d)
assert a2 not in d  # same hash, not equal

b1 = BClass(123, 'foo')
b2 = BClass(123, 'baz')
d = {b1: 100}
print(d)
print(b2)
assert b2 in d  # same hash and equal


print("=====")
d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
for k in d:
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

d = {'smtp': 21, 'dict': 2628, 'svn': 3690, 'ircd': 6667, 'zope': 9673}
try:  # the try clause should enclose the loop over dict block
    for k in d:
        # loop over a view, reflects the dict state
        if k == 'smtp':
            d['foo'] = 'baz'  # iterate over a view of the dict, fails
except Exception as e:
    print(repr(e))

for k in d:  # fails
    try:
        del d[k]
    except Exception:
        pass
