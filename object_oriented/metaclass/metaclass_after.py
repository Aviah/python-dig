# Use a metaclass to do things after class creation
# This is similar to class decorator, with the advantage of inheritance
class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        """Runs after the class was already created"""
        print(f"metaclass __init__ {cls}")
        print(f"name: {name}")
        print(f"bases: {bases}")
        print(f"attrs: {attrs}")
        for name, value in attrs.items():
            print(f"{name}:{value}")
        cls.bar = '123'  # Modify the created class


class AClass(metaclass=Metaclass):
    foo = 'baz'
    bar = 'abc'
    print("Creating AClass")  # Runs before the metaclass init


class Subclass(AClass):
    spam = 'eggs'
    print("Creating Subclass")  # Runs before the metaclass init


print(AClass.foo)
print(AClass.bar)
print(Subclass.foo)
print(Subclass.bar)

a = AClass()
s = Subclass()
print(a.bar)
print(s.bar)
