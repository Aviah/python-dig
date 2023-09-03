class Metaclass(type):
    """
    The class is ready, can do do something with the class object
    """

    def __init__(cls, name, bases, attrs):
        print(f"Metaclass __init__ invoked: {cls} | {name} | {bases} | {attrs}")

    def __new__(metacls, name, bases, attrs):
        """
        Call to the metaclass, to create the class
        """
        print(f"Metaclass __new__ invoked: {metacls} | {name} | {bases} | {attrs}")
        print("Creating class")
        return super().__new__(metacls, name, bases, attrs)  # same as type.__new__(...)

    def __call__(cls, *args, **kwargs):
        print(f"Metaclass __call__ invoked: {cls} | {args} | {kwargs}")
        return super().__call__(cls, *args, **kwargs)


class Base1:
    pass


class Base2:
    pass


class AClass(Base1, Base2, metaclass=Metaclass):
    print("Reading Aclass definitions...")
    foo = 'baz'

    def __new__(cls, *args, **kwargs):
        print(f"AClass __new__ invoked {args} | {kwargs}")
        print("Creating instance")
        inst = super().__new__(cls)  # note: w/o args. This is how Python works
        # Can modify the instance based on the args, kwargs
        return inst

    def __init__(self, *args, **kwargs):
        """
        The instance is ready, so return nothing
        """
        print(f"AClass __init__ invoked {args} | {kwargs}")

    def spam(self):
        return 'eggs'

    print("Done reading definitions")


print(AClass)  # class created


print("=====")
a = AClass(100)
print(a)


# see metaclass_instance_creation.py
