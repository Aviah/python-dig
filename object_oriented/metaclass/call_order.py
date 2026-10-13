class Metaclass(type):

    def __init__(cls, name, bases, attrs):
        print(f"Metaclass __init__ invoked: {cls} | {name} | {bases} | {attrs}")
        super().__init__(name, bases, attrs)

    def __new__(mcls, name, bases, attrs):
        """
        Call to the metaclass, to create the class
        Python treats __new__ as static method
        """
        print(f"Metaclass __new__ invoked: {mcls} | {name} | {bases} | {attrs}")
        print("Creating the class")
        return super().__new__(mcls, name, bases, attrs)  # same as type.__new__(...)

    def __call__(cls, *args, **kwargs):
        print(f"Metaclass __call__ invoked: {cls} | {args} | {kwargs}")
        return super().__call__(*args, **kwargs)


class Base1:
    pass


class Base2:
    pass


print("\n===== Class creation =====")

class AClass(Base1, Base2, metaclass=Metaclass):
    print("Reading AClass definitions...")
    foo = 'baz'

    def __new__(cls, *args, **kwargs):
        print(f"AClass __new__ invoked {args} | {kwargs}")
        print("Creating instance")
        inst = super().__new__(cls)  # note: w/o args. This is how Python works
        # Can modify the instance based on the args, kwargs
        return inst

    def __init__(self, *args, **kwargs):
        """
        The instance already exists, initialise it and return None
        """
        print(f"AClass __init__ invoked {args} | {kwargs}")

    def spam(self):
        return 'eggs'

    print("Done reading definitions")


print(AClass)  # class created


print("\n===== Instance creation =====")

a = AClass(100)
print(a)


# See class_creation.py, instance_creation.py
