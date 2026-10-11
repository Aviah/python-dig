class AClass:
    foo = 'baz'

    def __init__(self, bar):
        self.bar = bar

    def __setattr__(self, key, value):
        print(f"__setattr__ invoked: {key} | {value}")
        object.__setattr__(self, key, value)  # otherwise invoking self.__setattr__ will recurse


a = AClass(42)
a.x = 'yo'  # implicit call to magic method __setattr__
setattr(a, 'spam', lambda self: 42)
a.__dict__['callme'] = 'maybe'
assert hasattr(a, 'callme')  # bypassed __setattr__
AClass.woop = 'spoon'  # class attr assignment, implicit call to type.__setattr__ (see metaclass)
assert hasattr(AClass, 'woop')
AClass.__setattr__(a, 'pool', 'clip')  # explicit call to magic method __setattr__


print(dir(a))
print(vars(a))
print(a.__dict__)
assert all(hasattr(a, x) for x in ('foo', 'bar', 'x', 'spam', 'callme', 'pool', 'woop'))


print("\n=====")

a.foo = 'now'
print(a.foo)  # instance attr
print(vars(a))  # foo is an instance attr, and lookup will find it first
del a.__dict__['foo']  # manual delete of attr from instance
print(a.foo)  # now foo attr is found on the class
del AClass.foo  # using type.__delattr__
try:
    print(a.foo)
except AttributeError as e:
    print(repr(e))

print("\n=====")

class BClass:
    def __init__(self, spam):
        self.__dict__['spam'] = spam

    def __setattr__(self, key, value):
        if key == 'spam':
            raise AttributeError("Can't change attribute")
        object.__setattr__(self, key, value)


b = BClass('eggs')
try:
    b.spam = 'pool'
except AttributeError as e:
    print(repr(e))
print(b.spam)  #  BClass does not allow to reassign the spam attr
b.__dict__['spam'] = 'pool'  # bypass __setattr__
print(b.spam)
b.whatever = 'jump'
print(b.whatever)

# set attr via descriptor see descriptor_protocol.py
