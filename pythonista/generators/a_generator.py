# For async generators, see concurrency/asyncio/gen_async.py

def simple_generator():
    print("Simple generator invoked")
    try:
        while True:
            yield  # yields None. close() excepts here
            print("Execution is back to the generator")
            print("Generator is doing something")
    except GeneratorExit:
        print("Closed...")
        raise
    finally:
        print("And done!")

g = simple_generator()
print(g)
next(g)
print('---')
next(g)
print('---')
assert next(g) is None
print('---')
print("Closing the generator...")
g.close()
try:
    next(g)
except StopIteration as e:
    print(repr(e))  # consuming a closed generator raises StopIteration


print("\n=====")

def counter(start, max_value):
    print("counter invoked")
    crr = start
    while crr <= max_value:
        yield crr  # yields value
        crr += 1


d = counter(1, 5)
print(d)
print(next(d))
print(next(d))
for i in d:
    print(i)  # continue from where it left


print("\n=====")

def genx():
    yield "one"
    yield "two"
    yield "three"
    yield "done"

g = genx()
for _ in range(4):
    print(next(g))


print("\n----- Gen expression")
g = (x for x in range(1, 4))
while True:
    try:
        print(next(g))
    except StopIteration:
        break


print("\n-----")

g = (x for x in range(7, 15))
print(next(g))
print(next(g))
print(list(g))


print("\n=====")

def get_wishes(wishes):
    print("I'm ready master")
    while True:
        yield f"You have got {wishes} more wishes"
        wishes -= 1
        if wishes == 0:
            return  "No wishes left" # return stops the generator

genie = get_wishes(3)
print(genie)
print(next(genie))
print("--- got back ---")
print(next(genie))
print(next(genie))
try:
    next(genie)
except StopIteration as e:
    print(f"{repr(e)}: {e.value}")  # No wishes left
