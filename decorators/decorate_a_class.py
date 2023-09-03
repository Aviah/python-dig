# This could be easily done with simple inheritance
# But not when the modification is known only at runtime
# Class decorator is a simple alternative to metaclass
# Python has its own class decorators, like @dataclass


def double_it(self, x):
    print(f"Always stay true to {self}")
    return x * 2


def class_decorator(cls):
    cls.double_it = double_it
    return cls


@class_decorator
class AdvancedLinearAlgebra:
    pass


a = AdvancedLinearAlgebra()
print(a.double_it(100))

import datetime
import functools


def print_timestamp(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(datetime.datetime.now().isoformat())
        return func(*args, **kwargs)

    return inner


@print_timestamp
def tripple_it(x):
    return x * 3


print(tripple_it(1000))


def print_timestampe_for_methods(cls):
    print(vars(cls))
    print(dir(cls))
    print(cls.__dict__)
    for k, v in vars(cls).items():
        if callable(v):
            print(f"Decorating {cls}.{k}")
            setattr(cls, k, print_timestamp(v))

    return cls


@print_timestampe_for_methods
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
