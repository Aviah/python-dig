"""
__init__ is called *after* the object is already created by __new__
So it can only modify the object in-place: it must return None
__init__ is just a step in handling the caller a ready object, see metaclass/
"""

class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        print(f"Metaclass __init__ invoked: {cls}")
        super().__init__(name, bases, attrs)

    def __new__(mcls, name, bases, attrs):
        print(f"Metaclass __new__ invoked: {mcls}")
        return super().__new__(mcls, name, bases, attrs)


class AClass(metaclass=Metaclass):
    def __init__(self, *args, **kwargs):
        print(f"Aclass __init__ invoked: {self}")


a = AClass()
