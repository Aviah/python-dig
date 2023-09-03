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


# Note: In real code, use functools.wraps to decorate the inner function
