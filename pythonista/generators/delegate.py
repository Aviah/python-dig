def make_upper():
    print("make_upper invoked")
    while True:
        print("waiting")
        text = yield
        print(text.upper())


def my_text_util():
    print("my_text_util_invoked")
    # do something here
    yield from make_upper()  # allows to factor out the subgenerator code from the main func


m = my_text_util()
print(m)
m.send(None)
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


m = my_other_text_util()
next(m)  # like send(None)
m.send("all generalizations are false")
m.send("(lack of) money is the root of all evil")
m.throw(ValueError)  # delegated to subgenerator
m.send("I was born modest‚ but it didn’t last")
try:
    m.throw(GeneratorExit)  # GeneratorExit is not delegated, and the delegating generator is clodes
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
        print("close invoked")


def delegating(x, y):
    yield from Iterator(x, y)


g = delegating(100, 103)
next(g)
print(next(g))
print(next(g))
g.throw(GeneratorExit)
