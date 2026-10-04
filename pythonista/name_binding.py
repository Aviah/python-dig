# All assignments are just binding of a symbol, the name, to an object
# Any symbol can bind to any object
print(sum)
print(sum(range(10)))


def sum(m):
    from functools import reduce

    return reduce(lambda x, element: x + element * 10, m)


print(sum)
print(sum(range(10)))
import builtins

print(builtins.sum)
print(builtins.sum(range(10)))
sum = builtins.sum
print(sum)
print(sum(range(10)))


def my_max(m, builtin_max=max):
    # The evaluation of builtin_max happens only once, when max is still Python's builtin max
    print(f"Max of {m} is {builtin_max(m)}")
    return builtin_max(m)


max = my_max
max([10, 1, 2, 3, 4, 5])
print(max(['a', 'b', 'c']))

import inspect

print(inspect.signature(my_max))
print(max)
max = builtins.max
print(max([10, 1, 2, 3, 4, 5]))
print(max)
assert inspect.signature(my_max).parameters['builtin_max'].default is max


d = {'spam': 'bloop'}
m = d
print(m)
d['spam'] = 'jump'  # same object that both d and m are bind to
print(m)
d = {'spam': 'baz'}  # new object, m still binds to the previous
print(m)
n = m
m.clear()
print(m)
print(n)

class AClass:
    def __init__(self, x):
        self.x = x

    def item(self, k, v):
        self.x[k] = v


print(d)
a = AClass(d)
a.item('spam', 'eggs')
print(a.x)
print(d)
assert a.x is d
