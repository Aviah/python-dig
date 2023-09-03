import threading

lock = threading.Lock()
with lock:
    print("Protected action")


from contextlib import contextmanager


@contextmanager
def ignore_exceptions(*exceptions):
    try:
        yield
    except exceptions as e:
        print(f"Ignored: {repr(e)}")


import os

with ignore_exceptions(OSError):
    os.remove("nosuchfile.tmp")

d = {1: 'spam'}
with ignore_exceptions(ValueError, KeyError):
    x = 'abc'
    print(d[int(x)])

with ignore_exceptions(ValueError, KeyError):
    x = 200
    print(d[int(x)])


class ContextMan:
    def __init__(self, foo='baz', ignore_exceptions=False):
        # __init__ required only if the context manager accepts arguments
        self.foo = foo
        self.ignore_exceptions = ignore_exceptions

    def __enter__(self, foo='baz'):
        print(f"__enter__ {self.foo}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"__exit__ {self.foo}: {exc_type} | {exc_val} | {exc_tb}")
        if exc_type and self.ignore_exceptions:
            # to let the exception propagate do nothing
            print("Ignore exceptions")
            return True

    def mult(self, x):
        return self.foo * x


with ContextMan() as c:
    print(c)
    print(c.mult(4))

with ContextMan('spam'):
    print("hi")

with ContextMan('eggs', ignore_exceptions=True):
    int('abc')


@contextmanager
def contextman(foo, ignore_exceptions=False):
    try:
        print("enter contextman")
        yield
    except Exception as e:
        if ignore_exceptions:
            print(f"Ignoring exception {repr(e)}")
            return True
    finally:
        print("exit contextman")


with contextman('bar'):
    print('hello')

with contextman('bar', ignore_exceptions=True):
    assert False


class Connection:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        print(f"Open connection: {self.connection}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Close connection: {self.connection}")


class TempState:
    def __init__(self, state: dict):
        self.state = state
        self.orig_state = {**state}

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        for k in self.orig_state.keys():
            if k in self.state:
                self.state[k] = self.orig_state[k]
            else:
                del self.state[k]


state = {'max_rows': 1000}
connection = 'Postgresql'
print(state)
with Connection(connection):
    with TempState(state):
        state['max_rows'] = 100
        print(state)
        print(f"do something")
print(state)


with ContextMan('eggs'):
    int('abc')  # The context manager will propagate the exception
