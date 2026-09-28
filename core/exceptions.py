import traceback
import sys

def f(x):
    d = {1: 'spam'}
    try:
        print(d[int(x)])
    except (ValueError, KeyError) as e:
        print(repr(e))

f('1')
f(2)
f('abc')


class MyError(Exception):
    def __init__(self, *args, **kwargs):
        print(f"Enter MyError __init__: {self}, {args}, {kwargs}")


def foo(x):
    print(f"----- Enter foo {x}")
    try:
        v = int(x)
        if v > 100:
            raise MyError(x, v, eggs='spam')
        if v == 3:
            raise EnvironmentError(x, v, 'eggs')
        assert v == 2
    except AssertionError:
        print("Assertion failed")
    except EnvironmentError as e:
        print(repr(e))
        print(e.args)

    except MyError as e:
        if v >= 1000:
            raise RuntimeError() from e  # chain
        elif v >= 500:
            raise RuntimeError() from None
        else:
            raise
    except Exception as e:
        print("Enter exception clause...")
        print(repr(e))
        print([m for m in x])
        try:
            print(x[100])
        except:
            "Exception in exception"
    else:
        # Can try...except here in a separate clause
        print("Woopi! Everything OK")
    finally:
        print("Finally clause, done here")

print("\n===== Custom error =====")
foo(1)
foo('2')
foo('3')
foo('abc')
foo([100, 200])
print("All exceptions so far handled")

# ===== Chain exceptions =====
""""
foo(1000): Raise another exception, chaining
foo(500): Raise another exception, no chaining
foo(200): Re-raise the same exception
"""
# Uncomment to try:
# foo(1000)
# foo(500)
# foo(200)

# ===== Exception Group =====
print("===== Exception Group =====")
eg = ExceptionGroup(
    "top",
    (
        ValueError("foo"),
        TypeError("foo"),
        ExceptionGroup("parent1", (
            AssertionError("bar"),
            TimeoutError("bar"),
            ExceptionGroup("leaf1", (ValueError("spam"), ZeroDivisionError("spam"))),
            ExceptionGroup("leaf2", (ValueError("eggs"), ZeroDivisionError("eggs"))),
        )),
        ExceptionGroup("parent2", (ZeroDivisionError("bloop"), TimeoutError("bloop"))),
    )
)

print("---- Exception Group")
traceback.print_exception(eg, file=sys.stdout)
print("---- Subgroup")
traceback.print_exception(eg.subgroup((ValueError, TimeoutError)), file=sys.stdout)
try:
    raise eg
except Exception as e:
    print("Exception Group raised...")
    print(repr(e))


try:
    raise ValueError("eggs")
except* ValueError as eg:
    for exc in eg.exceptions:
        if str(exc) == 'spam':
            print("Handling ValueError spam")
        if str(exc) == 'eggs':
            print("Handling ValueError eggs")


try:
    raise ExceptionGroup("blah", (
        ValueError("spam"),
        TimeoutError()
    ))
except* ValueError:
    print("First handling ValueError")

except* TimeoutError:
    # except* does not run only the first match (like except)
    print("Then handling TimeoutError")

# ===== BaseExceptions that are not Exceptions =====
# Exception hierarchy: https://docs.python.org/3/builtins/exceptions.html#exception-hierarchy
print("\n===== BaseExceptions that are not Exceptions")
import atexit
def bye_bye():
    print("Bye Bye!")
atexit.register(bye_bye)

try:
    print(isinstance(KeyboardInterrupt(), BaseException))
    print(isinstance(KeyboardInterrupt(), Exception))
    raise KeyboardInterrupt()  # BaseException, but not Exception
except Exception as e:
    # Will never get here
    ...


