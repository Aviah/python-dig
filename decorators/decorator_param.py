import functools
from typing import Callable


def get_decorator(custom_greetings):
    def decorator(func):  # The common style is to call this function "outer"
        functools.wraps(func)

        def inner():
            print(custom_greetings)
            func()

        return inner

    return decorator


@get_decorator("Aloha!")  # Python expects this function to return the actual decorator function
def hi_there():
    print("Hi there!")


@get_decorator("Ciao!")
def hello():
    print("Hello!")


hi_there()
hello()
