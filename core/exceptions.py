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
        print(f"MyError __init__: {self}, {args}, {kwargs}")


def foo(x):
    print(f"===== {x}")
    try:
        v = int(x)
        if v > 100:
            raise MyError(x, v, eggs='spam')
        assert v == 2
        raise EnvironmentError(x, v, 'eggs')
    except AssertionError:
        print("Assertion failed")
    except EnvironmentError as e:
        print(e)
        print(e.args)

    except MyError as e:
        if v >= 1000:
            raise RuntimeError() from e  # chain
        elif v >= 500:
            raise RuntimeError() from None
        else:
            raise
    except Exception as e:
        print(e)
        print([m for m in x])
        try:
            print(x[100])
        except:
            "Exception in exception"
    else:
        print("Woopi! Everything OK")
    finally:
        print("Finally clause, done here")


foo(1)
foo('2')
foo('abc')
foo([100, 200])
print("=====")
print("All exceptions so far handled")


# Raise another exception, chaining
# foo(1000)

# Raise another exception, no chaining
# foo(500)

# Raise the same exception
foo(200)
