# LEGB: Local, Enclosing, Globals, Builtin

import sys


sum = 'sum global string'

def f1():
    sum = 'sum local string'
    print(sum)

def outer(x):
    sum = x

    def inner():
        print(sum)

    return inner


def f2():
    print(sum)


f1()  # local
outer(100)()  # enclosing
f2()  # global
m = sys.modules[__name__]
delattr(m, 'sum')
f2()  # builtin

print("\n===== Lexical scoping =====")

country = 'Laputa'
print(f"global: {country}")

def assume_global():
    print(f"assume_global: {country}")  # no local binding, Python will find scope from LEGB, here it's global
assume_global()

def outer():
    country = 'Luggnagg'
    print(f"outer: {country}")

    def c1():
        nonlocal country  # relates to enclosing scope that is not global
        country = 'Balnibarbi'
        print(f"c1: {country}")

    def c2():
        country = 'Glubdubdrib'
        print(f"c2: {country}")

    def c3():
        nonlocal country  # Optional: since there is no local assignment, Python will look for the next scope in LEGB
        print(f"c3: {country}")

    def c4():
        global country
        print(f"c4: {country}")

    def c5():
        global country
        country = 'Utopia'
        print(f"c5: {country}")

    def c6():
        # we do not need nonlocal, since country is not assigned in c6: Python does not consider it local
        print(f"c6: {country}")

    def c7():
        try:
            # Because country is assigned in c7, Python treats it as *local* to c7.
            # Here it is still not bound: the print will fail
            print(country)
        except UnboundLocalError as e:
            print(f"c7 raised: {repr(e)}")
        country = 'Never Neverland'
        print(f"c7: {country}")

    return c1, c2, c3, c4, c5, c6, c7

funcs = outer()
for f in funcs:
    f()
c3 = funcs[2]  # the closure keeps the correct ref to outer scope (which was changed in c1)
c3()
print(f"global: {country}")  # c5 changed the global scope


print('-----')

def outer():
    country = {'name': 'Never Neverland'}
    print(f"outer: {country['name']}")

    def c8():
        country['name'] = 'Utopia'  # mutating the same object, unlike local assignment: nonlocal is not needed here
        print(f"c8: {country['name']}")

    def c9():
        country = {'name': 'Luggnagg'}  # new local binding, no effect on outer scope
        print(f"c9: {country['name']}")

    def c10():
        print(f"c10: {country['name']}")

    return c8, c9, c10

funcs = outer()
for f in funcs:
    f()


"""
Classes do not use lexical scope. They have a namespace, and names become attributes.
Lookup is done via attributes lookup, not via lexical scope.

--- Will not work ---
class AClass:
    foo = 'baz'

    def print_foo(self):
        nonlocal foo  # wrong, the class is *not* an enclosing lexical scope
        print(foo)  # should be self.foo

"""


print("\n===== globals and locals")
# Useful for introspection

mdlvar = 'FOO'
assert 'mdlvar' in globals()
assert globals()['mdlvar'] == 'FOO'
print(globals())  # the current frame's global namespace, normally the module namespace
print(locals())
assert globals() is locals()  # on the module it's the same object
def f1():
    f1var = 'BAR'
    print(f"f1: {locals()}")
    def closure():
        nonlocal f1var
        nestedvar = 'SPAM'
        print(f"closure: {locals()}")
    return closure

class A:
    x = 100
    print(f"class A: {locals()}")

    def do_this_or_that(self):
        mthdvar = 'EGGS'
        print(f"method: {locals()}")

closure = f1()
closure()
A().do_this_or_that()