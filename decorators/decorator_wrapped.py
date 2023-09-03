import functools
from typing import Callable


def unwrapped(func: Callable):
    def inner():
        """I'm the inner of unwrapped"""
        print("Hello from unwrapped")
        return func()

    return inner


def wrapped(func: Callable):
    @functools.wraps(func)  # A builtin decorator
    def inner():
        """I'm the inner of wrapped"""
        print("Hello from wrapped")
        func()

    return inner


@unwrapped
def foo():
    """I'm foo"""
    print("Foo")


@wrapped
def baz():
    """I'm baz"""
    print("Baz")


foo()
baz()
print(f"My name is {foo.__name__}:  {foo.__doc__}")
print(f"My name is {baz.__name__}: {baz.__doc__}")  # wrapped
