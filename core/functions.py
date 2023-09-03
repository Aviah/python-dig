from typing import Callable
import sys


# functions are just objects
def foo():
    print("All generalizations are false")


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

print("=====")


def bar(f: Callable):  # can pass as an argument
    f()
    print("A quote by Mark Twain")


bar(foo)

from functools import partial

p = partial(bar, foo)
p()


print("=====")


# function is an object, and may have it's own attrs
def baz():
    return hasattr(baz, 'spam')


assert not baz()
baz.spam = 'eggs'
assert baz()
print(baz.__dict__)
