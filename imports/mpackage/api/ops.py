print(f"{__name__} imported")
from ..core import linear_algebra


def double_and_add_one(x):
    return linear_algebra.double_it(x) + 1
