import itertools

print("===== Generator Expressions =====")
g = (x for x in range(4))
print(g)
print(next(g))
print(next(g))
print([x for x in g])

print("\n-----")
print(sum(x for x in range(100)))


print("\n----- Infinite")
g = (x for x in itertools.cycle(('foo', 'baz', 'bar')))
print(next(g))
print(next(g))
print(next(g))
print(next(g))  # cycle, the generator wraps infinite itertools.cycle


print("\n===== Misc =====")

print("\n----- Gen func args")
def gen(seq):
    for element in seq:
        yield element
    print("meh")

g = gen(['foo', 'baz', 'bar'])
print(next(g))
print(next(g))
print(next(g))
try:
    print(next(g))
except StopIteration as e:
    print(repr(e))

print([x for x in g])


print("\n----- Sentinel, stop without StopIteration")
sentinel = object()
g = gen([100, 200, 300])
print(next(g, sentinel))
print(next(g, sentinel))
print(next(g, sentinel))
print(next(g, sentinel))
print(next(g, sentinel))

assert next(g, sentinel) is sentinel  # verify if a generator is empty w/o StopIteration

print("\n----- Generator inner loop")
def incr_gen(n):
    x = 0
    while x < n:
        yield x
        x += 1

g = incr_gen(8)
print(g)
print([x for x in g])

print("\n----- Infinite")
def infinite_gen():
    answer = 42
    print(f"Found the answer")
    while True:
        yield answer

for idx, element in enumerate(infinite_gen()):
    print(idx, element)
    if idx > 3:
        break  # otherwise infinite


print("\n===== Return Value =====")

def with_return_value():
    yield "All"
    yield "Generalizations"
    yield "Are"
    return "False"


g = with_return_value()
print(next(g))
print(next(g))
print(next(g))
try:
    next(g)
except StopIteration as e:
    return_value = e.value  # Python puts the generator returned value in StopIteration.value
    print(return_value)

print("\n-----")

def with_return_value2():
    try:
        yield "History"
        yield "doesn't"
        yield "repeat"
        yield "itself"
    except GeneratorExit:
        return "but it does rhyme."
    finally:
        print("Release resources etc")

g = with_return_value2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
return_value = g.close()
print(return_value)


print("\n===== Receive Values =====")
def format_text(func):
    print(f"format_text with *{func}* invoked")
    while True:
        print("Waiting...")
        text = yield
        if text == 'stop':
            return
        print(f"{getattr(text,func)()}")


g = format_text('capitalize')
print(g)
next(g)  # "prime" the generator, until the first yield
print("Primed...")
g.send('all generalizations are false')
g.send('lack of money is the root of all evil')
g.close()
try:
    next(g)
except StopIteration as e:
    print(repr(e))


print("\n-----")

g1 = format_text('upper')
g1.send(None)
print("Primed...")
g1.send("banana")
g1.send("strawberry")
try:
    g1.send('stop')
except StopIteration as e:
    print(repr(e))


print("\n-----")
g2 = format_text('title')
g2.send(None)
print("Primed...")
try:
    g2.send()
except TypeError as e:
    print(repr(e))
g2.send('foo bar spam eggs')
try:
    # Ultimately, the caller can just close() or throw() an exception. It can't kill the generator from outside
    g2.throw(GeneratorExit)
except GeneratorExit as e:
    print(repr(e))
