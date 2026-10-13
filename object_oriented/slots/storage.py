# __slots__ defines a fixed set of *instance* attributes up front,
# Instead of allowing arbitrary *instance* attributes through an instance __dict__.

class AClass:
    __slots__ = ('foo',)

    def __init__(self):
        # Even __init__ cannot create instance attributes outside __slots__
        try:
            self.bloop = 'blah'
        except AttributeError as e:
            print(repr(e))


class BClass:
    __slots__ = ('foo', 'bar')


class CClass:
    pass


a = AClass()
a.foo = 100
print(AClass.__dict__['foo'])
print(type(AClass.__dict__['foo']))  #  Python creates a "member_descriptor" for each slot

try:
    a.bar = 200
except AttributeError as e:
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
assert hasattr(a, '__slots__')  # Found on class
assert not hasattr(a, '__dict__')  #  *no instance dictionary*

dir(a)  # still works w/o instance dictionary, with attr lookup
try:
    vars(a)  # fails, the instance has no __dict__
except TypeError as e:
    print(repr(e))

delattr(a, 'foo')  # The slot member descriptor has __delete__
assert not hasattr(a, 'foo')