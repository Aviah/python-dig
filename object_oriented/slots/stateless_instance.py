# Empty __slots__ prevents instances from having instance attributes.
# They can still access class attributes and methods
# So the instance can act as a lightweight behavior only view of the class
# The class object itself remains mutable, and the instance can mutate the *class* as well

class AClass:
    __slots__ = ()
    x = 100

    def print_something(self):
        print('Something')

    @classmethod
    def print_something_else(self):
        print('Something else')


# Stateless instance
a = AClass()
a.print_something()
a.print_something_else()
print(a.bloop)

print(a.x)
print(a.__slots__)
try:
    a.x = 200  # read only
except AttributeError as e:
    print(repr(e))


print("\n=====")

# The class remains mutable
AClass.y = 300
print(AClass.y)
print(AClass().y)