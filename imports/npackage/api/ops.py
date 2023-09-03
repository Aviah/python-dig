print(f"{__name__} imported")
from ..core import linear_algebra

__all__ = ['double_and_add']


def double_and_add(x, y):
    return linear_algebra.double_it(x) + y


def say_hi():
    return 'hi'
