# A property on a metaclass acts as a computed property of the class object.
# Similar to a normal @property on an instance.
class Metaclass(type):
    num = 100

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
        return cls.num * 9


print(AClass.x)
print(BClass.x)
try:
    a = AClass()
    a.x
except AttributeError as e:
    print(e)  # metaclass property is available on AClass, not on its instances
