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
try:
    assert issubclass(AClass, object)
    assert isinstance(AClass, Meta)
    assert AClass.__repr__ is object.__repr__
    print(object.__repr__)
    print(AClass.__repr__())  # will *not* show AClass repr, since it goes to mro and not the type
except TypeError as e:
    print(repr(e))
print(type.__repr__(AClass))  # works, goes to the type
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
