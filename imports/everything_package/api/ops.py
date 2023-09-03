print(f"{__name__} imported")
from ..core import linear_algebra


def double_and_mult(x, y):
    return linear_algebra.double_it(x) * y


def say_hello():
    return 'hello'
