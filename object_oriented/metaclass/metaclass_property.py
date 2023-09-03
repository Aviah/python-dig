# Similar to using properties and class and accessor on instance
# Use property on metaclass for the class. Useful for functions like "MyClass.get_manager"
class Metaclass(type):
    num = 10

    @property
    def x(cls):
        return cls.mult_it()


class AClass(metaclass=Metaclass):
    @classmethod
    def mult_it(cls):
        return cls.num * 3


class BClass(metaclass=Metaclass):
    @classmethod
    def mult_it(cls):
        return cls.num * 10


print(AClass.x)
print(BClass.x)


# https://stackoverflow.com/questions/69940846/why-metaclass-works-for-a-class-propery-but-a-classmethod-property-doesnt
# https://stackoverflow.com/questions/50785774/property-setter-issues-in-metaclass
