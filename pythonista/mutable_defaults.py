
import inspect


def f(pos='default'):
    print(pos)
f()
f('foo')

print("\n===== None default =====")
def f1(elements, seq=None):
    if seq is None:
        seq = []
    seq.extend(elements)
    print(seq)

f1(['apple', 'cherry'])
f1(['apple', 'cherry'])
f1(['apple', 'cherry'], ['banana', 'strawberry', 'watermelon'])


print("\n===== List default =====")
def f2(elements, seq=[]):
    seq.extend(elements)
    print(seq)  # the default is persisted local list object

f2(['apple', 'cherry'])
f2(['apple', 'cherry'])
f2(['apple', 'cherry'])
f1(['apple', 'cherry'], ['banana', 'strawberry', 'watermelon'])


# seq points to a list object, which is created *once*, when Python creates the f2 function object
# Typically, with common code and flow, this default object is never replaced
print(f2.__defaults__)
print(inspect.signature(f2))
print(inspect.signature(f2).parameters['seq'])

print("\n=====")

class AClass:
    foo = []  # list default
    baz = 'bar'

a = AClass()
a.foo.append('spam')
print(a.foo)
b = AClass()
print(b.foo)
b.foo.append('eggs')
print(a.foo)
assert a.foo is b.foo
print(a.baz)
print(b.baz)
b.baz = 'whatever'
print(a.baz)
print(b.baz)


class BClass:

    def __init__(self):
        # No issue with the class attribute: it's created on the instance, with __init__
        self.lt = []
        self.dc = {}

a = BClass()
a.lt.append(1000)
a.dc['spam'] = 'eggs'
b = BClass()
print(b.lt)
print(b.dc)
assert 1000 not in b.lt
assert 'spam' not in b.dc
assert b.lt is not a.lt
assert b.dc is not a.dc


