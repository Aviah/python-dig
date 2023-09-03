class AClass:
    __slots__ = 'foo'


class BClass:
    __slots__ = ['foo', 'bar']


class CClass:
    pass


a = AClass()
a.foo = 100

try:
    a.bar = 200
except Exception as e:
    print(repr(e))

c = CClass()
c.bar = 200
print(c.bar)

b = BClass()
b.foo = 100
b.bar = 200
print(b.foo)
print(b.bar)

print(c.__dict__)
assert not hasattr(c, '__slots__')
assert hasattr(a, '__slots__')
assert not hasattr(a, '__dict__')

dir(a)  # works, attr lookup
try:
    vars(a)  # fail, a has no __dict__
except TypeError as e:
    print(repr(e))
