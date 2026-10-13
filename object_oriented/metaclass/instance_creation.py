class Metaclass(type):
    def __call__(cls, *args, **kwargs):
        """
        Will Calls the cls's __new__ method
        If new returns instance of this class (including subclass): invokes __init__
        """
        print(f"Metaclass __call__ invoked: {cls} | {args} | {kwargs}")
        return super().__call__(*args, **kwargs)


class AClass(metaclass=Metaclass):
    def __new__(cls, *args, **kwargs):
        # Python considers __new__ as static method
        print(f"AClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # will create the instance

    def __init__(self, *args, **kwargs):
        print(f"AClass __init__ invoked: {self} | {args} | {kwargs}")
        self.foo = kwargs.get('foo', None)


class BClass(AClass):
    def __init__(self, *args, **kwargs):
        print(f"BClass __init__ invoked: {self} | {args} | {kwargs}")
        self.spam = kwargs.get('spam', None)
        super().__init__(*args, **kwargs)


class CClass:
    def __new__(cls, *args, **kwargs):
        print(f"CClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        # Returns instance of *another* class, AClass
        # So the metaclass will not invoke it's __init__
        # AClass __init__ will not be invoked either: since object.__new__(AClass) just creates it
        return super().__new__(AClass)  # creates AClass instance

    def __init__(self, *args, **kwargs):
        print(f"CClass __init__ invoked: {self} | {args} | {kwargs}")
        self.bar = 'baz'


class DClass(metaclass=Metaclass):
    @classmethod
    def factory(cls, *args, **kwargs):
        print(f"DClass factory invoked: {cls} | {args} | {kwargs}")
        return cls(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        print(f"DClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance

    def __init__(self, *args, **kwargs):
        print(f"DClass __init__ invoked: {self} | {args} | {kwargs}")
        self.foo = kwargs.get('foo', None)


print("\n===== AClass instance =====")
a = AClass(123, foo='baz')
print(a)
print(a.foo)

print("\n===== BClass instance =====")
b = BClass(456, spam='eggs')
print(b)
print(b.foo)
print(b.spam)


print("\n===== CClass instance =====")
c = CClass()
assert isinstance(c, AClass)
assert not hasattr(c, 'foo')  # __init__ was not invoked
assert not(hasattr(c, 'bar'))
print(c)  # AClass instance


print("\n===== Instanciate from instance's class =====")

a1 = type(a)(foo='new')
print(a1)
print(a1.foo)


print("\n====== DClass with factory classmethod =====")

d = DClass.factory(foo='pool')
print(d)
print(d.foo)
