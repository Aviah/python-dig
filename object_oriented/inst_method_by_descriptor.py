class Foo:
    def __init__(self, x):
        self.x = x

    def double_it(self):
        return self.x * 2


print(type(Foo.double_it))
foo = Foo(100)
print(type(foo.double_it))  # This one is 'bound', the descriptor returned a function with an instance
print(foo.double_it())
f1 = Foo.double_it.__get__(foo)
print(type(f1))  # Same, we just used the descriptor manually, which is normally done by Python
print(f1())
print(foo.double_it is f1)
assert foo.double_it == foo.double_it
assert foo.double_it is not foo.double_it  # The descriptor returns different objects per every access: “is” fails
assert foo.double_it.__func__ == Foo.double_it  # Underlying func is the same, that's why "==" works
assert foo.double_it is not Foo.double_it
assert foo.double_it == f1
