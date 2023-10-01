# For custom classes, implicit invocations of special methods
# are only guaranteed to work correctly if defined on an object’s type
# https://docs.python.org/3.10/reference/datamodel.html#special-method-lookup
class Meta(type):
    def __repr__(cls):
        print("Meta __repr__ invoked")
        return type.__repr__(cls)


class AClass(metaclass=Meta):
    spam = 'eggs'
    pass


a = AClass()
print(a.__repr__)
print(a.__repr__())
print("=====")
print(type.__repr__(AClass))  # works, on the type
print("=====")
assert issubclass(AClass, object)
assert isinstance(AClass, Meta)
assert AClass.__repr__ is object.__repr__
print("-----")
print(repr(AClass))  # works on the type
print(object.__repr__)  # used by the instance with mro
print("-----")
print(AClass.__repr__(AClass))  # the type
print("-----")
print(type.__repr__(AClass))  # works on `type`, instead of Meta's __repr__ (no invoked message)
print("=====")
print(AClass.__mro__)
print(AClass.__bases__)


class BClass(AClass):
    def __repr__(self):
        print("BClass __repr__ invoked")
        return object.__repr__(self)


b = BClass()
print("=====")
print(repr(b))
print("=====")
print(object.__repr__(BClass))
print(type.__repr__(BClass))

print(b.spam)
print(BClass.spam)
print(object.__getattribute__(b, 'spam'))
print(type.__getattribute__(BClass, 'spam'))
print(object.__getattribute__(BClass, 'spam'))
