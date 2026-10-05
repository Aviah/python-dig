import time

def counter(max):
    print("Counter invoked...")
    crr = 0
    try:
        while crr < max:
            yield crr
            print("Counter resume...")
            crr += 1
    except GeneratorExit as e:
        print(f"Counter exit on {repr(e)}")
        raise

    except OSError as e:
        print(f"Counter OSError handler: {repr(e)}")
        raise

    except Exception as e:
        # The exception is handled, but the the generator is out of the while loop
        print(f"Counter general exceptions handler: {repr(e)}")

    else:
        print(f"Counter try-else clause invoked")

    finally:
        print(f"Counter finally clause invoked")

g = counter(3)
print(list(g))


print("\n=====")

g = counter(3)
print(next(g))
print(next(g))
try:
    g.throw(ValueError)
except StopIteration as e:
    print(repr(e))  #  The generator while loop excepted (even if the exception was handled)

print("\n=====")

g = counter(3)
print(next(g))
print(next(g))
try:
    g.throw(OSError("Oops"))
except OSError as e:
    print(repr(e))  # the generator re-raised the exception

print("\n=====")
def gen1():
    yield 1
    yield 2
    yield 3
    raise StopIteration

g = gen1()
print(next(g))
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration as e:
    print("Will not get here")
except RuntimeError as e:
    # The generator should just finish and return, Python raises the StopIteration error for the caller
    print("StopIteration raised *inside* a generator is converted to RuntimeError")


print("\n===== Exception clauses in generator =====")

def genx():
    print('Gen x invoked...')
    try:
        yield 'x-one'
        yield 'x-two'
        yield 'x-three'
    except Exception as e:
        print(f"Gen x excepted: {repr(e)}")
    else:
        print("Gen x try-else clause invoked")

    finally:
        print("Gen x finally clause invoked")

g = genx()
print(list(g))
print("Closing exhausted generator")
g.close()  # Nothing happens. The finally already ran when the list consumed the generator

print("\n-----")

g = genx()
print(next(g))
print("Closing not-exhausted generator")
g.close()  # finally runs with the close()


print("\n-----")

g = genx()
print(next(g))
try:
    g.throw(OSError)
except StopIteration as e:
    print(repr(e))


print("\n----- Yield in finally clause")

def geny():
    print('Gen y invoked...')
    try:
        yield 'y-one'
        yield 'y-two'
        yield 'y-three'
    except Exception as e:
        print(f"Gen y excepted: {repr(e)}")
        yield 'FOO (yielded by except clause)'
    else:
        print("Gen y try-else invoked")
        yield

    finally:
        print("Gen y finally invoked")
        yield 'SPAM (yielded by finally)'


print("\n----- Yield in finally")

g = geny()
print(next(g))
print("Closing not exhausted generator Gen y")
try:
    g.close()
except RuntimeError as e:
    print(f"Close when the finally clause yields raises Runtime error: {repr(e)}")


print("\n===== Except Clause =====")


print("\n----- Yield in except clause")
g = geny()
print(next(g))
print(g.throw(ValueError("foo")))  # The exception clause yields, the generator did not stop
print("-- After throw --")
print(next(g))  # finally yields, still not getting StopIteration
print("-- After finally --")
try:
    next(g)
except StopIteration as e:
    print(repr(e))


print("\n===== Generator Exit =====")

def genz():
    print("Gen z invoked")
    while True:
        try:
            yield 42
        except GeneratorExit as e:
            print(f"Gen z says: I ignore GeneratorExit! Ignoring: {repr(e)}")
            continue
        finally:
            print("Gen z finally clause invoked")


g = genz()
print(next(g))
print(next(g))
print(next(g))
print("Closing: 1st attempt...")
try:
    g.close()
except Exception as e:
    print(repr(e))  # Runtime error

print(next(g))
print(next(g))
print("Closing: 2nd attempt...")
try:
    g.close()
except Exception as e:
    print(repr(e))

print(next(g))
print(next(g))


print("Deleting generator...")
time.sleep(2)
del g  # f this removes the last ref to g, Python will attempt to close it just before it's garbage collected
time.sleep(2)
try:
    print(g)
except Exception as e:
    print(repr(e))
print("Finally deleted it. Exit")
# To execute the finally clause, Python will throw GeneratorExit before deleting the generator
# https://stackoverflow.com/questions/50091553/python-generators-garbage-collection
