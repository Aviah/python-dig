class MetaBase(type):
    callme = 'maybe'


class Meta(MetaBase):
    spam = 'eggs'


class AClass(metaclass=Meta):
    foo = 'baz'


class BClass(AClass):
    pass


# Metaclass attributes are available to the class
assert 'callme' not in dir(AClass)
assert 'spam' not in dir(AClass)
assert hasattr(AClass, 'callme')  # this is a glitch of the dir implementation  https://bugs.python.org/issue40098
assert hasattr(AClass, 'spam')
print(AClass.callme)
print(AClass.spam)
print(BClass.callme)
print(BClass.spam)


print("=====")
# type.__getattribute__ runs on the class, so follows mro
print(BClass.__mro__)
print(type.__getattribute__(BClass, 'foo'))  # by mro
print(type.__getattribute__(BClass, 'callme'))  # same, has access to metaclass attrs
try:
    print(type.__getattribute__(BClass(), 'callme'))
except TypeError as e:
    print(repr(e))  # type works on classes (type object)


# object.__getattribute__ on instance, so instance then *parent* mro: type(instance).__mro__
print("=====")
b = BClass()
print(type(b).__mro__)
print(object.__getattribute__(b, 'foo'))
print(object.__getattribute__(BClass, 'callme'))
try:
    print(object.__getattribute__(b, 'callme'))
except Exception as e:
    print(repr(e))

try:
    print(type(BClass).__mro__)
    print(object.__getattribute__(BClass, 'foo'))
except Exception as e:
    print(repr(e))
