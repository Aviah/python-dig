def make_upper():
    print("make_upper invoked")
    while True:
        print("waiting...")
        text = yield
        print(text.upper())


def my_text_util():
    print("my_text_util_invoked")
    # do something here
    yield from make_upper()  # allows to factor out the subgenerator code from the main func


m = my_text_util()
print(m)
m.send(None)  # delegating will call delegated's next
m.send('alL generaLiZationS are FAlse')
m.send('foo')


print("=====")


def make_title():
    print("make_title invoked")
    while True:
        try:
            text = yield
            if text == 'stop':
                raise StopIteration
            print(text.title())
        except ValueError as e:  # exceptions are delegated as well
            print(repr(e))
        except Exception as e:
            print(repr(e))
            raise


def my_other_text_util():
    yield from make_title()
    print("Delegated resumed")


m = my_other_text_util()
next(m)  # like send(None)
m.send("all generalizations are false")
m.send("(lack of) money is the root of all evil")
m.throw(ValueError)  # delegated to subgenerator
m.send("I was born modest‚ but it did not last")
try:
    m.close()
except GeneratorExit as e:
    pass

print("=====")


class Iterator:
    def __init__(self, start, end):
        self._crr, self._start, self._end = None, start, end

    def __iter__(self):
        return self

    def __next__(self):
        if self._crr is None:
            self._crr = self._start
        else:
            self._crr += 1

        if self._crr >= self._end:
            print("iterator done")
            raise StopIteration

        return self._crr

    def close(self):
        print("Delegated close invoked")


def delegating(x, y):
    try:
        yield from Iterator(x, y)
    except GeneratorExit as e:
        print(f"Delegating excepted on GeneratorExit of delegated: {repr(e)}")

    # can yield from other generators here


g = delegating(100, 104)
next(g)
g.send(None)  # 101, when send None, the delegating gen calls the delegated next
print(next(g))
print(next(g))
g.close()  # can use the GeneratorExit exception


print("====")
# after GeneratorExit


def delegating1(x, y):
    try:
        yield from IteratorYieldOnClose(x, y)
    except GeneratorExit as e:
        print(f"Delegating excepted on GeneratorExit of delegated: {repr(e)}")
        yield "Don't yield here"


class IteratorYieldOnClose(Iterator):
    def close(self):
        yield 100
        print("Will not get here")


class IteratorExceptOnClose(Iterator):
    def close(self):
        print("Raising on close")
        raise TypeError("spam")


g1 = delegating1(100, 104)
print(next(g1))
try:
    g1.close()  # can use the GeneratorExit exception
except RuntimeError:
    print("Yielding in close raises RuntimeError")

print("=====")


def delegating2(gen_class, x, y):
    delegated = gen_class(x, y)
    try:
        yield from delegated
    except GeneratorExit as e:
        print(f"Delegating excepted on GeneratorExit of delegated: {repr(e)}")
        raise EnvironmentError('foo')


print("=====")
g2 = delegating2(IteratorExceptOnClose, 100, 104)
print(next(g2))
try:
    g2.close()  # delegated raises another exception
except Exception as e:
    print(repr(e))

print("=====")
g3 = delegating2(Iterator, 100, 104)
print(next(g3))
try:
    g3.close()  # delegating raises another exception
except Exception as e:
    print(repr(e))
