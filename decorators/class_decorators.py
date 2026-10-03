# Class decorator is a simple alternative to metaclass
# Python has its own class decorators, like @dataclass
# Class decorators are useful when common modification/functionality to many unrelated classes, without inheritance

import datetime
import functools
import inspect


def double_it(self, x):
    print(f"Always stay true to {self}")
    return x * 2


def add_double_it_method(cls):
    cls.double_it = double_it
    return cls


@add_double_it_method  # Adds a method, no inheritance
class AdvancedLinearAlgebra:
    pass


a = AdvancedLinearAlgebra()
print(a.double_it(100))


def print_timestamp_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(datetime.datetime.now().isoformat())
        return func(*args, **kwargs)

    return inner


@print_timestamp_decorator
def triple_it(x):
    return x * 3

print(triple_it(1000))


def print_timestamp_for_methods(cls):
    print(vars(cls))
    print(dir(cls))
    print(cls.__dict__)
    for k, v in vars(cls).items():
        if inspect.isfunction(v):
            func = v
            print(f"Decorating {cls}.{k}")
            setattr(cls, k, print_timestamp_decorator(func))

    return cls


@print_timestamp_for_methods  # decorate all class methods
class AClass:
    def __init__(self, foo):
        print("__init__ invoked")
        self.foo = foo

    def say_hi(self):
        print(f"Hi {self.foo}")

    def say_hello(self):
        print(f"Hello {self.foo}")


a = AClass('spam')
a.say_hi()
a.say_hello()

print(AClass.say_hi)
print(a.say_hi)
print(AClass.say_hi.__qualname__)
