def simple_generator():
    print("simple generator invoked")
    while True:
        yield  # yields None
        print("back, running in the generator")
        print("generator is doing something")


g = simple_generator()
print(g)
next(g)
print('---')
next(g)
print('---')
next(g)
print('---')
assert next(g) is None
g.close()
try:
    next(g)
except StopIteration as e:
    print(repr(e))

print("=====")


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
print("=====")
for i in d:
    print(i)  # continue from where it left

print("=====")


def genx():
    yield "one"
    yield "two"
    yield "three"
    yield "done"


g = genx()
for _ in range(4):
    print(next(g))


print("=====")
g = (x for x in range(1, 4))  # same, with genexp
while True:
    try:
        print(next(g))
    except StopIteration:
        break


print("=====")
g = (x for x in range(7, 15))
print(next(g))
print(next(g))
print(list(g))


print("=====")


def get_wishes(wishes):
    print("I'm ready master")
    while True:
        yield f"You have got {wishes} more wishes"
        wishes -= 1
        if wishes == 0:
            return


genie = get_wishes(3)
print(genie)
print(next(genie))
print("--- got back ---")
print(next(genie))
print(next(genie))
try:
    next(genie)
except StopIteration as e:
    print(repr(e))  # return stops the generator
