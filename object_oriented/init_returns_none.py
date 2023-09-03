# __init__ is called *after* the object is already created
# So it can modify the object in-place, but should not return anything but None
class Metaclass(type):
    def __init__(cls, name, bases, attrs):
        print(f"__init__: {cls}")

    def __new__(cls, name, bases, attrs):
        print(f"__new__: {cls}")
        return super().__new__(cls, name, bases, attrs)


class AClass(metaclass=Metaclass):
    def __init__(self, *args, **kwargs):
        print(f"Aclass __init__: {self}")


a = AClass()
