import functools
from typing import Callable


def not_wrapped(func: Callable):
    def inner():
        """I'm the inner of not wrapped"""
        print("Hello from not wrapped")
        return func()

    return inner


def is_wrapped(func: Callable):
    @functools.wraps(func)  # A builtin decorator
    def inner():
        """I'm the inner of wrapped"""
        print("Hello from is wrapped")
        func()

    return inner


@not_wrapped
def foo():
    """I'm foo"""
    print("Foo")


@is_wrapped
def baz():
    """I'm baz"""
    print("Baz")


foo()
baz()
print(f"My name is {foo.__name__}:  {foo.__doc__}")
print(f"My name is {baz.__name__}: {baz.__doc__}")  # wrapped
