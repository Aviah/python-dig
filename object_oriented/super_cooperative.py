# Diamond
class AClass:
    def hello(self):
        print(f"Hello from A, self is: {self}")


class BClass(AClass):
    def hello(self):
        print(f"Hello from B, self is: {self}")
        super().hello()


class CClass(AClass):
    def hello(self):
        print(f"Hello from C, self is: {self}")
        super().hello()


class DClass(BClass, CClass):
    def hello(self):
        print(f"Hello from D, self is: {self}")
        super().hello()


class EClass:

    @classmethod
    def who_am_i(cls):
        # Inside a method, __class__ is the lexical scoped defining class
        # it allows the zero arguments super() to work with classes directly
        print(f"lexical __class__: {__class__}")
        print(f"runtime cls:       {cls}")
        print(f"type(cls):         {type(cls)}")

    @classmethod
    def factory(cls, *args, **kwargs):
        # sometimes it's useful to provide another way to create an instance (e.g. from json)
        print(f"EClass factory invoked: {cls} | {args} | {kwargs}")

        # In a class method super() is conceptually super(__class__, cls)
        # *Both* args are classes, then super continues as usual
        # __class__ provides the point in the mro after which lookup begins: it's fixed to lexical scope
        # cls supplies the actual class whose mro path is followed
        print(super())  # Conceptually super(__class__, cls)

        # Even with no explicit base class, the mro ends in "object".
        # So super() in a classmethod can continue from the class to object.
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance

    def __new__(cls, *args, **kwargs):
        # Python considers __new__ as a static method
        print(f"EClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())  # Conceptually super(__class__, cls)
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance

    def __init__(self, *args, **kwargs):
        print(f"EClass __init__ invoked: {self} | {args} | {kwargs}")
        self.foo = kwargs.get('foo', None)

    @classmethod
    def say_hello(cls):
        print(f"Say hello from EClass. Super:  {__class__}, {cls}")


class EClass1(EClass):
    @classmethod
    def say_hello(cls):
        print(f"Say hello from EClass1. Super: {__class__}, {cls}")
        super().say_hello()


class EClass2(EClass1):
    @classmethod
    def say_hello(cls):
        print(f"Say hello from EClass2. Super: {__class__}, {cls}")
        super().say_hello()

print("\n===== Simple super(): from subclass to parent =====")
b = BClass()
print(b)
b.hello()  # after B: A
print(BClass.__mro__)


print("\n===== Cooperative super(): walk-up the mro=====")
d = DClass()
print(d)
d.hello()  # After B: C
print(DClass.__mro__)

# The runtime object's type provides the mro path
# Lexical __class__ is pinned to the defining class, so it tells super where to continue lookup from in the mro
assert DClass.__mro__ is type(d).__mro__


print("\n===== Super and classmethod =====")
# In a classmethod, cls provides the runtime object who's mro path is followed
# When you start with instance, you first need it's class to get the mro
# Lookup on the mro continues after the class in which it was *defined* (lexically, not runtime)

e1 = EClass()
print(e1)
e1.who_am_i()

print("\n-----")
e2 = EClass.factory()
print(e2)

print("\n-----")
e3 = EClass2()
e3.say_hello()
