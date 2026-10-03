import functools


def decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print(f"Decorated! args: {args}, kwargs: {kwargs}")
        return func(*args, *kwargs)

    return inner


@decorator
def double_it(x):
    print(x * 2)

@decorator
def say_something(message):
    print(message)

double_it(10)
double_it(x=100)

say_something("All generalizations are false")
say_something(message="Bloop")