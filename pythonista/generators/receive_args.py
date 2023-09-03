def format_text(func):
    print(f"format_text with {func} invoked")
    while True:
        print("waiting...")
        text = yield
        if text == 'stop':
            return
        print(f"{getattr(text,func)()}")


print("=====")
g = format_text('title')
print(g)
next(g)  # "prime" the receiving arg generator, until the first yield
print("-- primed --")
g.send('all generalizations are false')
g.send('lack of money is the root of all evil')
g.close()
try:
    next(g)
except StopIteration as e:
    print(repr(e))

print("=====")
g1 = format_text('upper')
g1.send(None)  # "prime" generator, with send(None), same like first next(g)
print("-- primed --")
g1.send('all generalizations are false')
g1.send('lack of money is the root of all evil')
try:
    g1.send('stop')
except StopIteration as e:
    print(repr(e))


print("=====")
g2 = format_text('capitalize')
g2.send(None)
print("-- primed --")
g2.send('all generalizations are false')
try:
    g2.throw(GeneratorExit)
except GeneratorExit as e:
    print(repr(e))
