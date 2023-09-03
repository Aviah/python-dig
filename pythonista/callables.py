def double_it(x):
    return x * 2


class AdvancedLinearAlgebra:
    def __init__(self, x):
        self.x = x

    def __call__(self, mult):
        return self.x * mult


print(double_it(10))
print(double_it.__call__)
print(double_it.__call__(10))


a = AdvancedLinearAlgebra(10)
print(a(5))
print(a(10))


assert callable(double_it)
assert callable(AdvancedLinearAlgebra)
assert callable(a)
assert callable(list)
print(list.__call__((1, 2, 3)))


class Aclass:
    pass


assert callable(Aclass)
assert not callable(Aclass())


from functools import partial
from random import randint

print(randint(0, 100))
f = partial(randint, 0, 100)
print(f())
