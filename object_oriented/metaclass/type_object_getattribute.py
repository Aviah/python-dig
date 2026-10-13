# Normally use type for classes and object for instances


class MetaBase(type):
    callme = 'maybe'


class Metaclass(MetaBase):
    spam = 'eggs'


class AClass(metaclass=Metaclass):
    foo = 'baz'


class BClass(AClass):
    ...


# Metaclass attributes are available to the class
assert 'callme' not in dir(AClass)  # metaclass attributes do not appear in the results list of dir
assert 'spam' not in dir(AClass)
assert hasattr(AClass, 'callme')
assert hasattr(AClass, 'spam')
print(AClass.callme)
print(AClass.spam)
print(BClass.callme)
print(BClass.spam)


print("\n===== Using type =====")

# type.__getattribute__ performs specialised class-object lookup:
# it can search both the class mro and the metaclass mro.
print(BClass.__mro__)
print(type.__getattribute__(BClass, 'foo'))  # by mro
print(type.__getattribute__(BClass, 'callme'))  # same, has access to metaclass attrs
try:
    print(type.__getattribute__(BClass(), 'callme'))  # instance of BClass, not an instance of a metaclass
except TypeError as e:
    print(repr(e))


# object.__getattribute__ works on instances
print("\n===== Using object =====")

b = BClass()
print(type(b).__mro__)
print(object.__getattribute__(b, 'foo'))

# Works! Because object treats BClass as an ordinary object
# Lookup just follows it's type mro, which happens to be the metaclass
print(object.__getattribute__(BClass, 'callme'))

try:
    print(object.__getattribute__(b, 'callme'))  # Will not work from the BClass *instance*
except Exception as e:
    print(repr(e))

print(type(BClass).__mro__)
try:
    # Classes have a dual lookup path: subclass based, and their type based
    # object knows only to look for the instance type, which for BClass is not AClass
    print(object.__getattribute__(BClass, 'foo'))
except Exception as e:
    print(repr(e))
