import functools
from functools import wraps


def double_it(func):
    functools.wraps(func)

    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return inner


def square_it(func):
    functools.wraps(func)

    def inner(*args, **kwargs):
        return pow(func(*args, **kwargs), 2)

    return inner


@double_it
@square_it
def add_10(x):
    return x + 10


@square_it
@double_it
def add_20(x):
    return x + 20


print(add_10(1))
print(add_20(1))
