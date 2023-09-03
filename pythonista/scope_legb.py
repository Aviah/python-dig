# LEGB: Local, Enclosing, Globals, Builtin

import sys


def f1():
    sum = 'sum local string'
    print(sum)


def outer(x):
    sum = x

    def inner():
        print(sum)

    return inner


sum = 'sum global string'


def f2():
    print(sum)


f1()  # Local
outer(100)()  # Enclosing
f2()  # Global
m = sys.modules[__name__]
delattr(m, 'sum')
f2()  # builtin

print("=====")
# Lexical scoping
country = 'Laputa'


def outer():
    country = 'Luggnagg'

    def f3():
        nonlocal country  # relates to enclosing scope that is not global
        country = 'Balnibarbi'
        print(country)

    def f4():
        country = 'Glubdubdrib'
        print(country)

    def f5():
        print("f5 invoked")
        nonlocal country
        print(country)

    def f6():
        global country
        print(country)

    def f7():
        global country
        country = 'Utopia'
        print(country)

    def f8():
        try:
            print(country)  # w/o nonlocal, the variable is not defined
        except UnboundLocalError as e:
            print(repr(e))  # This exception is spot on! try print(abc)
        country = 'Never never land'
        print(country)

    return f3, f4, f5, f6, f7, f8


print(country)
funcs = outer()
[f() for f in funcs]
f5 = funcs[-4]
f5()
print(country)
"""
# Will not work
# Classes don't use lexical scope, but as attribute of an object. Here: self.foo
class AClass:
    foo = 'baz'

    def print_foo(self):
        nonlocal foo
        print(foo)
"""
