# Class based decorators are useful when decoration requires state, more complex behavior, or config args by the
# decoration expression (e.g. closure with "self" that is mutable)

class DoubleItDecorator:
    """
    __call__ returns the decorating function (the inner closure)
    """
    def __call__(self, func):
        # This is the callable that Python receive after evaluation of the decoration expression
        # It is used once per decoration: receives a (to be decorated) func object, and returns the decorating closure
        print(f"Enter {self.__call__.__qualname__}...")
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * 2

        return inner


@DoubleItDecorator()
def add_10(x):
    return x + 10

print(f"Decorated by: {add_10}")
print(add_10(1))
print(add_10(2))


print("=====")

class TripleItDecorator:
    """
    __call__ IS the decorating function
    """
    def __init__(self, func):
        # This is the callable that Python decoration syntax gets after evaluating the decoration expression
        # Here, Python receives the initialized instance as the decorating callable
        print(f"TripleIt __init__ invoked: {func.__name__}")
        # To wrap the instance, use:
        # functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        # Called when the decorating callable (the instance) is called instead of the decorated functionn
        print(f"Enter {self.__call__.__qualname__}...")
        return self.func(*args, **kwargs) * 3


# Python decoration expression calls the class, and gets the *instance* as the decorating callable
@TripleItDecorator
def add_20(x):
    return x + 20

print(f"Decorated by: {add_20}")
print(add_20(5))
print(add_20(6))

print("=====")

class MultipleItDecorator:
    def __init__(self, x):
        self.x = x

    def __call__(self, func):
        print(f"Enter {self.__call__.__qualname__}...")
        def inner(*args, **kwargs):
            return func(*args, **kwargs) * self.x

        return inner


# Python gets an initiated object, so the decorator call @ uses __call__
# The decorated function is the returned inner
@MultipleItDecorator(10)
def add_100(x):
    return x + 100


print(f"Decorated by: {add_100}")
print(add_100(7))
print(add_100(8))
