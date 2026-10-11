# https://docs.python.org/3/reference/datamodel.html#object.__lt__
class AClass:
    """Compare objects by len of a str attribute"""

    name: str

    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        print(f"{self}.__lt__")
        return len(self.name) < len(other.name)

    def __le__(self, other):
        print(f"{self}.__le__")
        return len(self.name) <= len(other.name)

    def __gt__(self, other):
        # comparisons are not assumed complementary - depends on implmentation
        print(f"{self}.__gt__")
        return len(self.name) >= len(other.name)  # >= for >

    def __eq__(self, other):
        print(f"{self}.__eq__")
        return len(self.name) == len(other.name)

    def __str__(self):
        return f"{self.__class__} object {self.name}>"


a = AClass('Brobdingnag')
b = AClass('Luggnagg')
c = AClass('Glubbdubdrib')
d = AClass('Glubbdubdrib')

print(a < b)
print(b < c)
print(d > c)
print(d == c)


class BClass(AClass):
    def __eq__(self, other):
        # Not an exception: tells Python to find elsewhere an alternative (it not NonImplementedError)g
        return NotImplemented


e = BClass('foo')
print(e == d)  # works, Python tries the other operand, here d.__eq__ exists and working
e1 = e
print(e1 == e)  # both return NotImplemented, fallback to "is" (identity)


print("\n-----")

class CClass:
    def __eq__(self, other):
        return 1, 2, 3  # Not obliged to return boolean, can return any object


print(CClass() == BClass('spam'))  # Uses CClass eq
assert (CClass() == CClass()) == (1, 2, 3)  # simply calls __eq__ as is with ==: returns the tuple (1,2,3)
if CClass() == BClass('eggs'):
    print("OK")  # With if, truthiness is required, so Python casts a non-empty tuple to True

print("\n-----")
print(a != b)  # __ne__ is missing, so object.__ne__ delegates to __eq__ and inverts the result



print("\n-----")

class DClass:
    def __eq__(self, other):
        return 42

print(CClass() == DClass())  # left to right
print(DClass() == CClass())  # left to right


print("\n----- Min/Max")

print(f"min is: {min(a, b, c, d, e)}")
print(f"max is {max(a, b, c, d, e)}")


print("\n===== Equality and hashing =====")
# If a == b, then must have hash(a) == hash(b), otherwise Python will not be able to access d[a] with d[b]
# If instances should remain hashable, a class that overrides __eq__ should also override __hash__
# Without custom __hash__ Python will make it unhashable
# So it enforce the developer to mathc hash to eq, or it will be non-hashable
# Note: hash collision is allowed, if hash(a) == hash(b) and a!=b. The otherway around is wrong

class EClass:
    """
    Demo class, breaks the rule:
    All instances are equal, but their hash may be different
    The equality and hashing behavior is totally customizable: even if breaks the logic!
    """

    def __init__(self, x):
        self.x = x

    def __eq__(self, othgger):
        # Any two instances of Eclass compared equal
        return True

    def __hash__(self):
        # When you define __eq__, must set __hash__, otherwise Python sets it to None
        return hash(self.x)  # Demo only: this is a


e1 = EClass('foo')
e2 = EClass('bar')
assert e1 == e2

# Should normally not happen if they are equal
# Note the != is likely, but Python allows hash collisions)
assert hash(e1) != hash(e2)

# Also breaks dict behavior
e3 = EClass(123)
e4 = EClass(456)
d = {e3: 100}
print(d)
assert e3 == e4  # __eq__ always returns True
assert hash(e3) != hash(e4)  # breaks the Python rule: if a == b, must have hash(a) == hash(b)
try:
    d[e4]
except KeyError as e:
    # Broken eq-hash
    # Should not happen, dictionaries should provide the value of k1 with k2 if k1==k2
    print(repr(e))

