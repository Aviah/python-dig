def counter(max):
    print("counter invoked")
    crr = 0
    try:
        while crr < max:
            yield crr
            print("back to counter")
            crr += 1
    except GeneratorExit as e:
        print(f"counter exit on {repr(e)}")
        raise

    except OSError as e:
        print(f"counter excepted on {repr(e)}")
        raise

    except Exception as e:
        print(f"counter ignoring {repr(e)}")

    else:
        print(f"counter try-else clause invoked")

    finally:
        print(f"counter finally clause invoked")


print(list(counter(3)))


print("=====")
g = counter(3)
print(next(g))
print(next(g))
try:
    g.throw(ValueError)
except StopIteration as e:
    print(repr(e))  # the generator ignored, but stopped on the except clause

print("=====")
g = counter(3)
print(next(g))
print(next(g))
try:
    g.throw(OSError)
except OSError as e:
    print(repr(e))  # the generator raised the exception


def genx():
    print('genx involved')
    try:
        yield 'xone'
        yield 'xtwo'
        yield 'xthree'
    except Exception as e:
        print('gen x excepted')
    else:
        print("genx try-else invoked")

    finally:
        print("genx finally invoked")


print("=====")
g = genx()
print(list(g))
g.close()

print("=====")
g = genx()
print(next(g))
print("closing not exhausted generator")
g.close()


print("=====")
g = genx()
print(next(g))
try:
    g.throw(OSError)
except StopIteration as e:
    print(repr(e))


print("=====")


def geny():
    print('geny involved')
    try:
        yield 'yone'
        yield 'ytwo'
        yield 'ythree'
    except Exception as e:
        print('gen y excepted')
        yield 'excepted'
    else:
        print("geny try-else invoked")
        yield

    finally:
        print("geny finally invoked")
        yield 'foo'


g = geny()
print(list(geny()))
g.close()

print("=====")
g = geny()
print(next(g))
print("closing not exhausted generator geny")
try:
    g.close()
except RuntimeError as e:
    print(repr(e))  # close when the finally clause yields, raises Runtime error

print("=====")
g = geny()
print(next(g))
g.throw(ValueError)  # The exception clause yields, the generator did not stop
print("-- after throw --")
print(next(g))  # finally yields, still not getting StopIteration
print("-- after finally --")
try:
    next(g)
except StopIteration as e:
    print(repr(e))


print("=====")


def genz():
    try:
        print("genz invoked")
        while True:
            yield 42
    except GeneratorExit:
        print("genz ignoring GeneratorExit")


g = genz()
print(next(g))
g.close()
try:
    print(next(g))
except StopIteration as e:
    print(repr(e))


print("=====")
g = counter(3)
next(g)
next(g)
next(g)

import time

print("deleting generator...")
time.sleep(2)
del g  # finally clause is executed when it is garbage collected
time.sleep(2)
print("exit")
# To execute finally, Python will throw GeneratorExit before deleting the generator
# https://stackoverflow.com/questions/50091553/python-generators-garbage-collection
