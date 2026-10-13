# Use a metaclass to modify/inspect/background handling after the class was created
# Note: Class decorator also provides "after creation modification",
# But metaclass is automatic, more robust, and has the advantage of auto running on subclasses
class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        """Runs after the class was already created"""
        print(f"metaclass __init__ invoked for {cls}")
        print(f"name: {name}")
        print(f"bases: {bases}")
        print(f"attrs: {attrs}")
        for name, value in attrs.items():
            print(f"{name}:{value}")
        cls.bar = '123'  # Modify the created class
        print(f"Metaclass changed attr: {cls}.bar to '123'")
        super().__init__(name, bases, attrs)


print("\n=====")

class AClass(metaclass=Metaclass):
    foo = 'baz'
    bar = 'abc'
    print("Creating AClass")  # Runs before the metaclass init


print("\n=====")

# Metaclass invokes for subclasses automatically (a class decorator does not)
class Subclass(AClass):
    spam = 'eggs'
    print("Creating Subclass")  # Runs before the metaclass init


print("\n=====")

print(AClass.foo)
print(AClass.bar)
print(Subclass.foo)
print(Subclass.bar)

a = AClass()
s = Subclass()
print(a.bar)
print(s.bar)
assert 'bar' in Subclass.__dict__  # The metaclass set it, although it didn't appear in Subclass definition