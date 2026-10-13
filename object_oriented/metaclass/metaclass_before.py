# Use a metaclass to control the class object before it is created.
from pprint import pp

class Metaclass(type):
    def __new__(mcls, name, bases, attrs):
        # Call to the metaclass, to create the class
        # Gives you almost complete control over class creation
        print(f"__new__: {mcls} | {name} | {bases} | {attrs}")
        return super().__new__(mcls, 'CClass', (), {'__module__': '__main__', '__qualname__': 'CClass'})


class Aclass(metaclass=Metaclass):
    pass


class BClass(Aclass):
    pass


class CClass:
    pass

# __new__ can completely ignore what it was asked to do!
assert Aclass.__name__ == 'CClass'
assert BClass.__name__ == 'CClass'
assert Aclass is not BClass
assert not issubclass(BClass, Aclass)
assert type(BClass) is Metaclass

a = Aclass()
print(a)
b = BClass()
print(b)
print(b.__class__)
print(type(b))
print(id(CClass))
print(id(b.__class__))
assert b.__class__ is not CClass  # same displayed name, different class objects


print("\n=====")

pp(globals())
print(id(Aclass), id(BClass), id(CClass))