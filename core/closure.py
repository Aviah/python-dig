def add_constant(x):
    def inner(m):
        return x + m

    return inner


f1 = add_constant(100)
print(f1(1))
print(f1(1000))

f2 = add_constant(1000)
print(f2(1))
print(f2(1000))

# __closue__ refers to values from outer scope, None if not
assert add_constant.__closure__ is None
print(f"f1.__closure__[0].cell_contents: {f1.__closure__[0].cell_contents}")  # 100 from the outer func scope

# caveat about late binding closures: https://docs.python-guide.org/writing/gotchas/#late-binding-closures


# The first closure lost lexical access to the x closure cell, so once it's set - you can't change it
# But we can provide lexical access to it

def add_constant(x):
    def inner(m):
        return x + m

    def set_x(value):
        nonlocal x
        x = value

    return inner, set_x

f3, set_x = add_constant(111)
print(f"f3.__closure__[0].cell_contents: {f3.__closure__[0].cell_contents}")  # 100 from the outer func scope
print(f3(1))
print(f3(1000))
set_x(222)
print(f"f3.__closure__[0].cell_contents: {f3.__closure__[0].cell_contents}")  # 100 from the outer func scope
print(f3(1))
print(f3(1000))
