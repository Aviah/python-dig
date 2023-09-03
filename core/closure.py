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
