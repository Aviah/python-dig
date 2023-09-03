# Diamond
class AClass:
    def hello(self):
        print("Hello from A")


class BClass(AClass):
    def hello(self):
        print(f"Hello from B, self is: {self}")
        super().hello()


class CClass(AClass):
    def hello(self):
        print("Hello from C")
        super().hello()


class DClass(BClass, CClass):
    def hello(self):
        print("Hello from D")
        super().hello()


class EClass:
    @classmethod
    def factory(cls, *args, **kwargs):
        # sometimes it's useful to provide another way to create an instance
        # e.g. create instance from a json config, or slower validations that should be used in special cases
        # for regular code just use return Dclass(*args, **kwargs)
        print(f"EClass factory invoked: {cls} | {args} | {kwargs}")
        # it's a class method, super() will not work
        # we provide the class as both the instance AND the type
        print(super(cls, cls))
        assert super(cls, cls).__new__ is object.__new__
        return super(cls, cls).__new__(cls)  # creates the instance

    def __new__(cls, *args, **kwargs):
        # Python considers __new__ as static method
        print(f"EClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance, python by design requires this format

    def __init__(self, *args, **kwargs):
        print(f"EClass __init__ invoked: {self} | {args} | {kwargs}")
        self.foo = kwargs.get('foo', None)


b = BClass()
print(b)
b.hello()  # after B: A
print(BClass.__mro__)
print("=====")
d = DClass()
print(d)
d.hello()  # After B: C
print(DClass.__mro__)
assert DClass.__mro__ is type(d).__mro__  # super follows mro, calculate from the instance type, it's __class__
print("=====")
e1 = EClass()
print(e1)
e2 = EClass.factory()
print(e2)
