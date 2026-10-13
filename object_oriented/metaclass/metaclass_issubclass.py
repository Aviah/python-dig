# Control issubclass behaviour
# Returning False can reject the real subclass
# Return NotImplemented to let Python continue with the normal check
# Note: With the addition of Protocol, it allows to define "structural relationship" with type checkrs
# subclass still allows to do that during code execution

print("\n===== With metaclass =====")

class AClass:
    pass


class FakeSubclassMetaclass(type):
    def __subclasscheck__(cls, subclass):
        # Here an arbitrary example, any subclass of AClass is considered True
        # Actually useful if you want to decide if issubclass based on the existence of specific attribute
        # e.g. issubclass of  iterator if hasattr __iter__
        # Note: ABC's implementation will call __subclasshook__
        # See https://docs.python.org/3/library/abc.html#abc.ABCMeta.__subclasshook__
        return issubclass(subclass, AClass)


class FakeSubclass(metaclass=FakeSubclassMetaclass):
    pass


class FClass(FakeSubclass):
    pass


assert not issubclass(FClass, FakeSubclass)
assert issubclass(AClass, (FakeSubclass, FClass))


print("\n===== Abstract class/method =====")

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
