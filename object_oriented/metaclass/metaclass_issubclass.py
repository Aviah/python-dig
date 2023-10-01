class AClass:
    pass


class FakeSubclassMeta(type):
    def __subclasscheck__(self, subclass):
        # Here an arbitrary example, any subclass of AClass is considered True
        # Actually useful if you want to decide if issubclass based on the existence of specific attribute
        # e.g. issubclass of  iterator if hasattr __iter__
        # Used in metaclass. Note: ABC's implementation will call __subclasshook__
        # See https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__
        return issubclass(subclass, AClass)


class FakeSubclass(metaclass=FakeSubclassMeta):
    pass


class FClass(FakeSubclass):
    pass


assert not issubclass(FClass, FakeSubclass)
assert issubclass(AClass, (FakeSubclass, FClass))


from abc import ABC, abstractmethod


class FakeSubclassABC(ABC):
    @classmethod
    def __subclasshook__(cls, C):
        return issubclass(C, AClass)

    @abstractmethod
    def mult(self, x, y):
        pass


class MyFakeSubclass(FakeSubclassABC):
    def mult(self, x, y):
        return x * y * 100


assert not issubclass(MyFakeSubclass, FakeSubclassABC)
assert issubclass(AClass, FakeSubclassABC)
