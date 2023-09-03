class AClass:
    foo = 'baz'

    def __init__(self, bar):
        self.bar = bar

    def __setattr__(self, key, value):
        print(f"__setattr__ invoked: {key} | {value}")
        self.__dict__[key] = value  # setattr will recurse


a = AClass(42)
a.x = 'yo'
setattr(a, 'spam', lambda self: 42)
a.__dict__['callme'] = 'maybe'
AClass.woop = 'spoon'
AClass.__setattr__(a, 'pool', 'clip')

print(dir(a))
print(vars(a))
print(a.__dict__)
assert hasattr(a, 'foo')
assert hasattr(a, 'bar')
assert hasattr(a, 'x')
assert hasattr(a, 'spam')
assert hasattr(a, 'callme')
assert hasattr(a, 'pool')
assert hasattr(a, 'woop')
assert all(hasattr(a, x) for x in ('foo', 'bar', 'x', 'spam', 'callme', 'pool', 'woop'))

print("=====")
a.foo = 'now'
print(vars(a))  # foo is an instance attr, and lookup will find it first
del a.__dict__['foo']
print(a.foo)  # now found on the class
print("=====")


class BClass:
    def __init__(self, spam):
        self.__dict__['spam'] = spam

    def __setattr__(self, key, value):
        if key == 'spam':
            raise AttributeError("Can't change attribute")


b = BClass('eggs')
try:
    b.spam = 'pool'
except AttributeError as e:
    print(repr(e))
print(b.spam)

# set attr via descriptor see descriptor_protocol.py
