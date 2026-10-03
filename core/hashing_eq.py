class AClass:
    def __init__(self, x: int, y: str):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash(self.x)

    def __eq__(self, other):
        return self.y == other.y


class BClass(AClass):
    def __hash__(self):
        # When defining custom __eq__, Python sets __hash__ to None, even if parent class *has* __hash__
        # To enable hashing, have to explicitly define it
        return hash(self.x)

    def __eq__(self, other):
        return self.x == other.x


a1 = AClass(123, 'foo')
a2 = AClass(123, 'baz')
d = {a1: 100}
print(d)
assert a2 not in d  # same hash, not equal

b1 = BClass(123, 'foo')
b2 = BClass(123, 'baz')
d = {b1: 100}
print(d)
print(b2)
assert b2 in d  # same hash and equal

print("=====")
lst = [1, 2, 3, 4]
s = {100, 200}
try:
    s.add(lst)
except Exception as e:
    print(repr(e))

class Foo:
    def __init__(self):
        self.lst = [1, 2, 3, 4]

foo = Foo()
print(foo.lst)

try:
    # equality for list is value based, [1, 2] == [1, 2]. Can't hash - the value is mutable
    s.add(foo.lst)
except Exception as e:
    print(repr(e))

# equality is *identity* based, can hash, the identity is immutable
s.add(foo)
print(s)
