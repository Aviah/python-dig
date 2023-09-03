# confusing, type/object relations provide creation and all the attributes for classes and instances
# for classes: both as types (type) and also as an instance (object)
# for instances: just objects (object)
two = 2
print(type(two))
print(dir(two)[:10])
print(vars(type(two))['__repr__'])

print("=====")
print(object)
print(object.__class__)
print(object.__bases__)
print(object.__mro__)

print("=====")
print(type)
print(type.__class__)
print(type.__bases__)
print(type.__mro__)
assert issubclass(type, object)

print("=====")


class AClass:
    pass


assert isinstance(AClass, type)
assert type(AClass) is type
assert isinstance(AClass(), object)
assert type(AClass()) is AClass
assert not isinstance(AClass, AClass)
assert not isinstance(list, list)
assert isinstance(type, type)
assert isinstance(object, object)
assert isinstance(type, object)
assert isinstance(object, type)
print(AClass)
print(AClass.__class__)
print(AClass.__bases__)
print(type.__class__)
print(object.__class__)
print("=====")
print(list)
print(type(list))
print(list.__class__)
print(list.__bases__)
print(list.__mro__)

print("=====")
# primitive objects
try:
    type.__new__ = lambda x: x
except TypeError as e:
    print(repr(e))

try:
    object.__new__ = lambda x: x
except TypeError as e:
    print(repr(e))
