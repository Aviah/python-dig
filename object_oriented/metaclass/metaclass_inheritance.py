"""
And another one (I promise this is the last wrinkle in the metaclass determination).
For new-style metaclasses, there is a constraint that the chosen metaclass is equal to,
or a subclass of, each of the metaclasses of the bases. Consider a class C with two base classes, B1 and B2.
Let's say M = C.__class__, M1 = B1.__class__, M2 = B2.__class__.
Then we require issubclass(M, M1) and issubclass(M, M2).
(This is because a method of B1 should be able to call a meta-method defined in M1 on self.__class__,
even when self is an instance of a subclass of B1.)
https://www.python.org/download/releases/2.2/descrintro/#metaclasses
"""


class Metaclass(type):
    pass


class MetaclassSubclass(Metaclass):
    pass


class Someclass(MetaclassSubclass):
    pass  # Works, use simple line inheritance


print(Someclass)
print(type(Someclass))
assert issubclass(Someclass, Metaclass)
assert type(Someclass) is not Metaclass  # Someclass is the subclass
print(Someclass.__class__)
print(Someclass.__class__.__class__)
print("=====")


class Metaclass1(type):
    def intro1(cls):
        print("Metaclass1 invoked")


class Metaclass2(type):
    def intro2(cls):
        print("Metaclass2 invoked")


class AClass(metaclass=Metaclass1):
    @classmethod
    def call_my_meta1(cls):
        type(cls).intro1(cls)


class BClass(metaclass=Metaclass2):
    @classmethod
    def call_my_meta2(cls):
        type(cls).intro2(cls)


try:
    # conflict
    class ConflictClass(AClass, BClass):
        pass

except TypeError as e:
    print(repr(e))  #

print("=====")


class UnifiedMetaclass(Metaclass1, Metaclass2):
    pass


class CClass(AClass, BClass, metaclass=UnifiedMetaclass):
    pass  # Works


print(CClass)
c = CClass()
c.call_my_meta1()
c.call_my_meta2()
