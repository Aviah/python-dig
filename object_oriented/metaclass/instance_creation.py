class Metaclass(type):
    def __call__(cls, *args, **kwargs):
        print(f"Metaclass __call__ invoked: {cls} | {args} | {kwargs}")
        # Calls the cls's __new__ method, and if it returns instance of this class - invoke __init__
        return type.__call__(cls, *args, **kwargs)


class AClass(metaclass=Metaclass):
    def __new__(cls, *args, **kwargs):
        # Python considers __new__ as static method
        print(f"AClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance

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
        return super().__new__(AClass)  # returns instance of *another* class, metacls will not invoke it's __init__

    def __init__(self, *args, **kwargs):
        print(f"CClass __init__ invoked: {self} | {args} | {kwargs}")
        self.bar = 'baz'


class DClass(metaclass=Metaclass):
    @classmethod
    def factory(cls, *args, **kwargs):
        print(f"DClass factory invoked: {cls} | {args} | {kwargs}")
        return DClass(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        # Python considers __new__ as static method
        print(f"DClass __new__ invoked: {cls} | {args} | {kwargs}")
        print(super())
        assert super().__new__ is object.__new__
        return super().__new__(cls)  # creates the instance

    def __init__(self, *args, **kwargs):
        print(f"AClass __init__ invoked: {self} | {args} | {kwargs}")
        self.foo = kwargs.get('foo', None)


print("Classes are ready")
print("=====")
print("Creating intances...")
a = AClass(123, foo='baz')
print("Creating instances...")
print("=====")
b = BClass(456, spam='eggs')
print("=====")
print(a)
print(b)
print(a.foo)
print(b.foo)
print(b.spam)
print("=====")
c = CClass()
assert not hasattr(c, 'foo')  # __init__ was not invoked
# instance from instance
print("=====")
a1 = a.__class__.__new__(a.__class__)
print(a)
print(a1)
print("======")
d = DClass.factory()
print(d)
