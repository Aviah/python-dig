import sys


class Ploop:
    pass


class AClass:
    def __init__(self, foo, bar, baz, spam):
        # recommended: declare all in __init__
        self.foo = foo
        self.bar = bar
        self.baz = baz
        self.spam = spam


class BClass:
    pass


class CClass:
    def set_attrs(self, foo, bar, baz, spam):
        self.foo = foo
        self.bar = bar
        self.baz = baz
        self.spam = spam


class DClass(CClass):
    def __init__(self):
        # recommended: declare all in __init__
        self.foo = None
        self.bar = None
        self.baz = None
        self.spam = None


values = (Ploop(), ['a', 'b', 'c'], 12345678, 'eggs')
a = AClass(*values)
b = BClass()
b.foo, b.bar, b.baz, b.spam = values
c = CClass()
c.set_attrs(*values)
d = DClass()
d.set_attrs(*values)
print(vars(a))
print(vars(b))
print(vars(c))
print(vars(d))
print(sys.getsizeof(values))
print(sys.getsizeof(a))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))
