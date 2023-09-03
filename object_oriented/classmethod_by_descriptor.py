class Foo:
    @classmethod
    def classic(cls):
        print(f"I am class {cls}")

    @staticmethod
    def double_it(x):
        return x * 2

    def everybody(self):
        print(f"I am instance {self}")


class Baz:
    pass


print(type(Foo.classic))
print(type(Foo.double_it))
print(type(Foo.everybody))

print("=====")
f1 = Foo()
f2 = Foo()
# @classmethod descriptor binds to the original class
Foo.classic.__get__(Foo)()
Foo.classic.__get__(Baz)()
Foo.classic.__get__(f1)()

# Call simple method: the descriptor returns instance-bound function
Foo.everybody.__get__(Foo)()
Foo.everybody.__get__(Baz)()
Foo.everybody.__get__(f1)()
Foo.everybody.__get__(f2)()

print("=====")
assert Foo.everybody is Foo.everybody  # the descriptor itself
assert Foo.everybody is not f1.everybody
assert f1.everybody is not f1.everybody
assert Foo.classic is not Foo.classic  # descriptor return new instances
assert f1.classic is not f1.classic
assert Foo.classic is not f1.classic
assert Foo.double_it is f1.double_it  # static function, as is
assert f1.double_it is f1.double_it
assert Foo.double_it.__get__(Baz) is not Foo.double_it.__get__(Baz)
