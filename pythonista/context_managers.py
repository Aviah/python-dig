from contextlib import contextmanager
import os
import threading

lock = threading.Lock()
with lock:
    print("Protected action")


@contextmanager
def ignore_exceptions(*exceptions):
    try:
        yield
    except exceptions as e:
        print(f"Ignored: {repr(e)}")



with ignore_exceptions(OSError):
    os.remove("nosuchfile.tmp")

d = {1: 'spam'}
with ignore_exceptions(ValueError, KeyError):
    x = 'abc'
    print(d[int(x)])

with ignore_exceptions(ValueError, KeyError):
    x = 200
    print(d[int(x)])

print("=====")
class ContextMan:
    def __init__(self, foo='baz', ignore_exceptions=False):
        # __init__ is useful when the context manager uses arguments
        self.foo = foo
        self.ignore_exceptions = ignore_exceptions

    def __enter__(self):
        print(f"__enter__, foo is: {self.foo}")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"__exit__, foo is: {self.foo}: {exc_type} | {exc_val} | {exc_tb}")
        if exc_type and self.ignore_exceptions:
            # to let the exception propagate do nothing
            print(f"Ignore exception: {repr(exc_type)}")
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
            print(f"Ignoring exception {repr(e)}")  # no need to return True with contextlib
        else:
            raise
    finally:
        print("exit contextman")


with contextman('bar'):
    print('hello')

with contextman('bar', ignore_exceptions=True):
    x = y

try:
    with ContextMan('eggs'):
        int('abc')  # The context manager will propagate the exception
except Exception as e:
    print(repr(e))


print("=====")
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
        self.state.clear()
        self.state.update(self.orig_state)


state = {'max_rows': 1000}
connection = 'PostgreSQL'
print(state)
with Connection(connection):
    with TempState(state):
        state['max_rows'] = 100
        print(state)
        print(f"do something")
print(state)

