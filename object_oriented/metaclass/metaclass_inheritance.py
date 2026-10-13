"""
And another one (I promise this is the last wrinkle in the metaclass determination).
For new-style metaclasses, there is a constraint that the chosen metaclass is equal to,
or a subclass of, each of the metaclasses of the bases.

Consider a class C with two base classes, B1 and B2:
* Let's say M = C.__class__, M1 = B1.__class__, M2 = B2.__class__.
* Then we require issubclass(M, M1) and issubclass(M, M2).

This is because a method of B1 should be able to call a meta-method defined in M1 on self.__class__,
even when self is an instance of a subclass of B1.)

BDFL From https://www.python.org/download/releases/2.2/descrintro/#metaclasses
"""

print("===== Subclassing metaclass =====")

class Metaclass(type):
    pass


class MetaclassSubclass(Metaclass):
    pass


class Someclass(metaclass=MetaclassSubclass):
    pass  # Uses MetaclassSubclass as its metaclass


assert issubclass(MetaclassSubclass, Metaclass)  # subclassing
assert type(MetaclassSubclass) is type  # instance-of

print(Someclass)
print(type(Someclass))
assert type(Someclass) is MetaclassSubclass
print(Someclass.__class__)
print(Someclass.__class__.__class__)

print("\n===== Metaclass conflict =====")

class Metaclass1(type):
    def intro1(cls):
        print("Metaclass1 invoked")


class Metaclass2(type):
    def intro2(cls):
        print("Metaclass2 invoked")


class AClass(metaclass=Metaclass1):
    @classmethod
    def call_my_meta1(cls):
        cls.intro1()


class BClass(metaclass=Metaclass2):
    @classmethod
    def call_my_meta2(cls):
        cls.intro2()


try:
    # conflict
    class ConflictClass(AClass, BClass):
        pass
except TypeError as e:
    print(repr(e))


print("===== Resolving metaclass conflict =====")

class UnifiedMetaclass(Metaclass1, Metaclass2):
    pass


class CClass(AClass, BClass, metaclass=UnifiedMetaclass):
    pass  # Works


# Works, CClass has access to all it's bases metaclasses behavior
assert type(CClass) is UnifiedMetaclass
assert issubclass(UnifiedMetaclass, Metaclass1)
assert issubclass(UnifiedMetaclass, Metaclass2)

print(CClass)
c = CClass()
c.call_my_meta1()
c.call_my_meta2()



