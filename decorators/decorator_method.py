import datetime
import functools


def print_invocation_timestamp(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"{func.__qualname__} invoked on {datetime.datetime.now().isoformat()}")
        return func(*args, **kwargs)

    return inner


class AClass:
    _counter = 0

    def __new__(cls, *args, **kwargs):
        cls._counter += 1
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name

    @classmethod  # The descriptor takes the decorated function
    @print_invocation_timestamp
    def counter(cls):
        return cls._counter

    @staticmethod
    @print_invocation_timestamp
    def double_it(x):
        return x * 2

    @print_invocation_timestamp
    def say_hi(self):
        return f"Hi {self.name}"


a = AClass('John')
b = AClass('Paul')
print(b.counter())
print(b.double_it(100))
print(b.say_hi())
