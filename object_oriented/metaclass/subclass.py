

class Metaclass(type):

    def __new__(mcls, name, bases, attrs, **kwargs):

        foo = kwargs.pop('foo', None)
        print(f"Metaclass __new__ invoked for {name}: {foo}")

        # Remaining kwargs are forwarded here through type.__new__.
        # type.__new__ will call __init_subclass__ (before calling __init__)
        return super().__new__(mcls, name, bases, attrs, **kwargs)


    def __init__(cls, name, bases, attrs, **kwargs):
        print(f"Metaclass __init__ invoked for {cls.__name__}")
        super().__init__(name, bases, attrs)


class AClass(metaclass=Metaclass, foo='FOO'):  # instance of metaclass, kwargs to config it

    def __init_subclass__(cls, **kwargs):
        # **kwargs are forwarded here through type.__new__

        bar = kwargs.pop('bar', None)
        print(f"{__class__.__name__} __init_subclass__ invoked for {cls.__name__}: {bar}")
        super().__init_subclass__(**kwargs)


class BClass(AClass, bar='BAR'):  # subclass, kwargs to config __init_subclass__
    ...


class CClass(AClass, bar='BAZ'):
    ...


print("\n=====")

class OtherClass(metaclass=Metaclass, foo='PRIVATE'):

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

try:
    class OfOther(OtherClass, spam='EGGS'):
        ...
except TypeError as e:
    print(repr(e))  # __init_subclass__ must consume the kwargs, or not pass them further


print("\n=====")

class DClass(AClass, bar='BARRR'):

    def __init_subclass__(cls, **kwargs):
        # *kwargs are passed here with new

        pool = kwargs.pop('pool', None)  # cooperative
        print(f"{__class__.__name__} __init_subclass__ invoked for {cls.__name__}: {pool}")
        super().__init_subclass__(**kwargs)


class EClass(DClass, bar='JUMP', pool='JUMPJUMP'):
    ...
