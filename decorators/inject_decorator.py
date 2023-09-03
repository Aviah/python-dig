# General purpose function that injects any function as a decorator
import functools


def inject_as_decorator(inject_func):
    def get_decorator(*args, **kwargs):  # Same as decorator_param.py
        def decorator(func):  # It's common to call this function "outer"
            @functools.wraps(func)
            def inner():
                inject_func(*args, **kwargs)
                return func()

            return inner

        return decorator

    return get_decorator


@inject_as_decorator  # Now the decorated function is a decorator (get_decorator closure)
def custom_greetings(greetings: str, times: int):
    print(f"{greetings} " * times)


@custom_greetings("Aloha!", 2)
def hi_there():
    print("Hi there!")


@custom_greetings("Ciao!", 5)
def hello():
    print("Hello!")


hi_there()
hello()
