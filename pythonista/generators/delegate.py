
print("\n===== Simple delegation =====")
def sub_generator():
    print("Sub-generator invoked")
    times = 3
    counter = 1
    while counter <= times:
        yield f"Sub-generator response: {counter}"
        counter += 1

    return "Excellent result"

def delegating_generator():
    print("Delegating generator invoked")
    result = yield from sub_generator()
    # Get here only after the sub-generator finished
    print("Delegating generator says: Sub-generator finished")
    print(f"Result len is: {len(result)}")
    return result

g = delegating_generator()
print(next(g))
print(next(g))
print(next(g))

try:
    next(g)
except StopIteration as e:
    print(f"Delegator returned: {e.value}")


print("\n===== Delegating exceptions =====")
def sub_generator1():
    yield 1
    yield 2
    return 100

def delegator1():

    try:
        yield from sub_generator1()  # delegator discards the sub-generator return value
    except StopIteration as e:
        print("Will never get here")

g = delegator1()
try:
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(f"Result: {e.value}")  # None, the delegator discarded this return value


print("\n===== Receive and return values =====")

def make_upper_case():
    print("make_upper_case invoked")
    text = yield   # First text
    while True:
        print("make_upper_case is waiting...")
        text = yield text.upper()  # returns the result, and also wait here to get the new text
        print("make_upper_case got the text, resume...")


def my_text_util():
    print("my_text_util_invoked")
    print("Prep resources etc...")
    yield from make_upper_case()  # allows to factor out functionality to another function
    # yield from is a "dumb pipe": Will get here only after my_upper_case is done (and not after each yield)


m = my_text_util()
print(m)
m.send(None)
print(m.send('alL generaLiZationS are FAlse'))
print(m.send("foo bAr SpaM eGGs"))


print("\n===== Generator Exit =====")

def make_title():
    print("make_title invoked")
    while True:
        try:
            text = yield
            if text == 'stop':
                return
            print(text.title())
        except ValueError as e:  # exceptions are delegated as well
            print(f"make_title says: {repr(e)}")
        except Exception as e:
            print(repr(e))
            raise
        finally:
            print("make_title finally clause invoked")


def my_other_text_util():
    try:
        yield from make_title()
    except GeneratorExit as e:
        print(f"my_other_text_util says: {repr(e)}")


m = my_other_text_util()
next(m)  # like send(None)
m.send("all generalizations are false")
m.send("(lack of) money is the root of all evil")
m.throw(ValueError("Wrong text"))  # delegated to sub-generator
m.send("I was born modest‚ but it didn’t last")
try:
    print("Throwing GeneratorExit...")
    m.throw(GeneratorExit)  # GeneratorExit is not delegated: yield from closes the delegated generator
except StopIteration as e:  # The delegating function continues and handle GeneratorExit
    pass


print("\n===== Delegating close =====")

class SimpleIterator:
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
        print("SimpleIterator.close() invoked")


def delegating(x, y):
    yield from SimpleIterator(x, y)


g = delegating(100, 103)
next(g)
print(next(g))
print(next(g))
g.close()  # yield from call close() on the delegated