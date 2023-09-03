from functools import wraps


def decorator(func):
    def inner(*args, **kwargs):
        print("Decorated!")
        return func(*args, *kwargs)

    return inner


@decorator
def double_it(x):
    print(x * 2)


double_it(10)
double_it(100)
