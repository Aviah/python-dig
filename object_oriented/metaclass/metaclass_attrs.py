class Metaclass(type):
    meta_attr = 'baz'

    def __init__(cls, name, bases, attrs):
        print(attrs)  # 'foo' will not be provided on b = Bclass()
        print(f"foo in attrs: {'foo' in attrs}")  # Only for AClass
        print(hasattr(cls, 'foo'))


class AClass(metaclass=Metaclass):
    foo = 'baz'


class Subclass(AClass):
    pass  # will call the metaclass, but w/o foo


class CClass(metaclass=Metaclass):
    def __init__(self, foo):  # __init__ is an attribute
        self.foo = foo


print(AClass.foo)
print(vars(AClass)['foo'])  # own attr
print(Subclass.foo)  # mro
a = AClass()
b = Subclass()
c = CClass(42)
print(c.foo)


print("=====")  # see type_object_getattribute
assert hasattr(Metaclass, 'meta_attr')
# instances of Metaclass
assert isinstance(AClass, Metaclass)
assert hasattr(AClass, 'meta_attr')
assert isinstance(Subclass, Metaclass)
assert hasattr(Subclass, 'meta_attr')
assert isinstance(CClass, Metaclass)
assert hasattr(CClass, 'meta_attr')
# *not* instances of Metaclass
assert not hasattr(a, 'meta_attr')
assert not hasattr(b, 'meta_attr')
assert isinstance(b, Subclass)
assert issubclass(Subclass, AClass)
assert hasattr(b, 'foo')
