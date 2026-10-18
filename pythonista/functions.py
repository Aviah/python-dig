import functools
from itertools import starmap, zip_longest
from typing import Callable
from functools import partial, reduce, singledispatch
from itertools import filterfalse

import sys


print("\n===== Functions are objects =====")

def foo():
    print("All generalizations are false")

# introspection

foo()
print(foo)
print(type(foo))
print(dir(foo))
print(foo.__name__)
print(foo.__qualname__)
print(foo.__module__)
foo.spam = 'eggs'

assert sys.modules[__name__].foo is foo
foo.__call__()


print("\n-----")

def bar(f: Callable):  # can pass as an argument
    f()
    print("A quote by Mark Twain")
bar(foo)


print("\n-----")

# As objects, functions can have their own attributes.
def baz():
    return hasattr(baz, 'spam')


assert not baz()
baz.spam = 'eggs'
assert baz()
print(baz.__dict__)
assert hasattr(baz, '__get__')  # this allows functions to be methods, see descriptors


print("\n===== Anonymous functions =====")
# lambda can't contain a return statement; its body is a single expression,
# whose value is returned automatically.

print([(lambda x: x * x)(x)  for x in range(10)])
print(list(filter(lambda x: (len(x) >= 3 if isinstance(x, str) else x >= 3), ['foo', 1, 'baz', 2, 'spam', 4, 'eggs', 4])))


print("\n===== Functional tools =====")

def x_squared(x):
    return pow(x, 2)


def x_exp_y(x, y):
    return pow(x, y)

print(list(map(x_squared, range(10))))
print(list(map(x_exp_y, range(5), range(5))))
print(list(starmap(x_exp_y, [(10, x) for x in range(10)])))  # *unpacks

exp_3 = partial(x_exp_y, y=3)
exp_4 = partial(x_exp_y, y=4)

print(list(map(exp_3, range(10))))
print(list(map(exp_4, range(10))))

print(list(filter(lambda x: x % 5 == 0, range(100))))
print(list(filterfalse(lambda x: x % 2 == 0, range(100))))

print(reduce(lambda x, y: x + y, range(10)))  # 1 + 2 + 3... sum(range(10))

d = {'foo': 1, 'baz':2, 'spam': 3, 'eggs': 4}
print(list(zip(d.keys(), d.values())))  # essentially d.items()
print(list(zip(range(5), range(10))))
print(list(zip_longest(range(5), range(10))))


print("\n===== Single dispatch =====")
# One generic function with implementations selected by the type of the first argument.
# Other arguments do not participate in dispatch.

@singledispatch
def do_something(x, y):
    ...

@do_something.register
def _(x: int, y):
    print(f"x is int, also {y}")

@do_something.register
def _(x: str, y):
    print(f"x is str, also {y}")

@do_something.register
def _(x: list, y):
    print(f"x is list, also {y}")

do_something(1, "blah")
do_something('foo', "blah")
do_something([1, 2, 3], "blah")
