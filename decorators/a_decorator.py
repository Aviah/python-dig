from typing import Callable


def the_decorator(func: Callable):
    def inner():
        print("Before the decorated func")
        print(func)
        results = func()
        print("After the decorated func")
        return results

    print(inner)
    return inner  # A decorator is just a closure


def hi_there():
    print("Hi there!")

"""
The @ syntax evaluates the decoration expression and expects to get from it a callable that:
1. Accepts an object to decorate (here it's the function hello)
2. Returns the "decoration" object that will replace the original (the now decorated)
"""
@the_decorator
def hello():
    print("Hello!")


hello()

# The symbol "hello" is bound to the inner function
print(hello)
print(hello.__name__)


hi_there()  # The original function
decorated = the_decorator(hi_there)  # Manually, instead of using @
decorated()
print(decorated)

# Note: In real code, use @functools.wraps to decorate the inner function
