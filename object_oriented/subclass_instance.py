class AClass:
    pass


class BClass:
    pass


class CClass(AClass, BClass):
    pass


a = AClass()
b = BClass()
c = CClass()

assert isinstance(a, AClass)
print(type(a))
print(a.__class__)

assert isinstance(AClass, type)
print(type(AClass))
print(AClass.__class__)

assert isinstance(c, CClass)
print(type(c))
print(c.__class__)

assert isinstance(CClass, type)
print(type(CClass))
print(CClass.__class__)


assert issubclass(CClass, AClass)
print(CClass.__bases__)
assert issubclass(CClass, (AClass, BClass))
assert not issubclass(CClass, type)
assert issubclass(CClass, object)
print(CClass.__mro__)
