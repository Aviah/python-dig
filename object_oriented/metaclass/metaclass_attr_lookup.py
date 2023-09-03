# Classes are an *instance* of the metaclass, so attr lookup from class continues to the metaclass
# But not for the class instance
class Metaclass(type):
    foo = 'baz'


class AClass(metaclass=Metaclass):
    pass


class Subclass(AClass):
    pass


a = AClass()
s = Subclass()
assert hasattr(AClass, 'foo')  # AClass is an *instance* of the metaclass, declared with the `metaclass=` arg: ok
assert hasattr(Subclass, 'foo')  # Subclass is a subclass of an instance of the metaclass, simple inheritance: ok
assert not hasattr(a, 'foo')  # 'a' is an *instance of an instance* of the metaclass: attr lookup stops at Aclass
assert not hasattr(s, 'foo')  # same
