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
        print(f"{self}.__lte__")
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
        return NotImplemented


e = BClass('foo')
print(e == d)
e1 = e
print(e1 == e)  # defaults to is


class CClass:
    def __eq__(self, other):
        return (1, 2, 3)


# Calls __eq__ to the object that has the method
print(CClass() == BClass('spam'))  # mustn't return bool
if CClass() == BClass('eggs'):
    print("OK")  # python bool conversion of a non empty tuple

print("=====")
print(a != b)  # When __ne__ is missing, use reflective method if subclass

print("=====")


class DClass:
    def __eq__(self, other):
        return 42


print(CClass() == DClass())  # left to right
print(DClass() == CClass())  # left to right

print("=====")
print(f"min is: {min(a, b, c, d, e)}")
print(f"max is {max(a, b, c, d, e)}")


class EClass:
    def __init__(self, x):
        self.x = x

    def __hash__(self):
        # When you define __eq__, must set __hash__, otherwise Python sets it to None
        return hash(self.x)

    def __eq__(self, other):
        return True


e1 = EClass(123)
e2 = EClass(123)
d = {e1: 100}
print(d)
print(e1)
assert e1 is not e2
print(d[e2])
