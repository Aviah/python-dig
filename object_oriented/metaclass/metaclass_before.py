# Use a metaclass to do things pre-class creation
class Metaclass(type):
    def __new__(metacls, name, bases, attrs):
        # Call to the metaclass, to create the class
        print(f"__new__: {metacls} | {name} | {bases} | {attrs}")
        return super().__new__(metacls, 'CClass', (), {'__module__': '__main__', '__qualname__': 'CClass'})


class Aclass(metaclass=Metaclass):
    pass


class BClass(Aclass):
    pass


class CClass:
    pass


a = Aclass()
print(a)
b = BClass()
print(b)
assert b.__class__ is CClass
