def f(pos='default'):
    print(pos)


f()
f('foo')


def f1(elements, seq=None):
    if seq is None:
        seq = []
    seq.extend(elements)
    print(seq)


fruits = ['banana', 'strawberry', 'watermelon']
f1(['apple', 'cherry'])
f1(['apple', 'cherry'], fruits)
f1(['apple', 'cherry'], fruits)
f1(['apple', 'cherry'], fruits)
print(fruits)  # global list
print("=====")
f1(['apple', 'cherry'], fruits[:])  # passes a copy of fruits


def f2(elements, seq=[]):
    if seq is None:
        seq = []
    seq.extend(elements)
    print(seq)


print("=====")
f2(['apple', 'cherry'])
f2(['apple', 'cherry'])
f2(['apple', 'cherry'])
f2(['apple', 'cherry'])  # seq is persistent across function calls
import inspect

# seq points to a list object, which is part of the function's signature object
# this list object is created once and never replaced
print(inspect.signature(f2))
print(inspect.signature(f2).parameters['seq'])


class AClass:
    foo = []
    baz = 'bar'


print("=====")
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
