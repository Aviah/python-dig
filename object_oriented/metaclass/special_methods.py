# For custom classes, implicit invocations of special methods
# are only guaranteed to work correctly if defined on an object’s type
# https://docs.python.org/3.10/reference/datamodel.html#special-method-lookup
class Metaclass(type):
    def __repr__(cls):
        print("Meta __repr__ invoked")
        return type.__repr__(cls)


class AClass(metaclass=Metaclass):
    spam = 'eggs'
    pass


a = AClass()
print(a.__repr__)
print(a.__repr__())


print("\n=====")

print(type.__repr__(AClass))  # works, on the type


print("\n=====")

assert issubclass(AClass, object)
assert isinstance(AClass, Metaclass)
assert AClass.__repr__ is object.__repr__
print("-----")
print(repr(AClass))  # works on the type
print(object.__repr__)  # used by the instance with mro
print("-----")

# Explicitly calls object.__repr__ with AClass as its argument.
# It bypasses the metaclass special-method lookup.
print(AClass.__repr__(AClass))  # the type
print("-----")
print(type.__repr__(AClass))  # works on `type`, instead of Meta's __repr__ (no invoked message)


print("\n=====")

print(AClass.__mro__)
print(AClass.__bases__)


class BClass(AClass):
    def __repr__(self):
        print("BClass __repr__ invoked")
        return object.__repr__(self)


b = BClass()


print("\n=====")

print(repr(b))


print("\n=====")

print(object.__repr__(BClass))
print(type.__repr__(BClass))

print(b.spam)
print(BClass.spam)
print(object.__getattribute__(b, 'spam'))
print(type.__getattribute__(BClass, 'spam'))
try:
    # object thinks that BClass is ordinary object
    # Follows instance-of mro, and not subclass-of mro
    print(object.__getattribute__(BClass, 'spam'))
except AttributeError as e:
    print(repr(e))