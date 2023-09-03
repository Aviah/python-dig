import functools


class DoubleIt:
    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * 2

        return inner


# __call__ is the callable that receives a (to be decorated) func object
# and returns the inner closure
@DoubleIt()
def add_10(x):
    return x + 10


print(add_10(1))

print("=====")


class TripleIt:
    def __init__(self, func):
        print(f"TripleIt __init__ invoked: {func.__name__}")
        functools.update_wrapper(self, func)  # The instance is the wrapper callable
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs) * 3


# The decorator call @ inits the class,  like call with TripleIt()
# The decorated function (the "inner")  is actually the __call__ method
@TripleIt
def add_20(x):
    return x + 20


print(add_20(5))

print("=====")


class MultipleIt:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * self.x

        return inner


# Python gets an initiated object, so the decorator call @ uses __call__
# The decorated function is the returned inner
@MultipleIt(10)
def add_100(x):
    return x + 100


print(add_100(7))
