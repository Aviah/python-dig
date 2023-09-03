class Metaclass(type):
    def __prepare__(name, bases, **attrs):
        print(f"Metaclass __prepare__ invoked: {name} | {bases} | {attrs}")
        # can return a special kind of dict
        # attrs manipulation can be done b4 creation on __new__, and after on __init__
        namespace = type.__prepare__(name, bases, **attrs)
        print(namespace)
        # When the final class object is created with __new__, namespace is *copied* into a new dict
        # Thus, if namespace is a special kind of dict: useful in the metaclass, but not once the class is created
        # https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace
        return namespace

    def __new__(mtcls, name, bases, attrs):
        """Create the class object, can modify the class creation args before it's created"""
        print(f"Metaclass __new__ invoked: {mtcls} | {name} | {bases} | {attrs}")
        assert super().__new__ is type.__new__
        cls = type.__new__(mtcls, name, bases, attrs)
        print(cls)  # cls was created
        return cls

    def __init__(cls, name, bases, attrs):
        """Can modify the new but already created class object, inplace (so returns None)"""
        print(f"Metaclass __init__ invoked: {cls} | {name} | {bases} | {attrs}")


class AClass:
    pass


class BClass:
    pass


class CClass(AClass, BClass, metaclass=Metaclass):
    foo = 'bar'

    def spam(self):
        return f"{self.foo} eggs"


c = CClass()
print(c.spam())
