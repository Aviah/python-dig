class Metaclass(type):
    def __instancecheck__(cls, instance):
        print(f"Metaclass __instancecheck__ invoked: {cls, instance}")
        return hasattr(instance, 'spam')  # can implement anything that evaluates to bool


class AClass(metaclass=Metaclass):
    pass


class BClass:
    pass


class CClass:
    spam = 'bar'


a = AClass()
b1 = BClass()
c = CClass()

assert isinstance(a, AClass)  # Not invoked: Python auto returns isinstance == True for direct descendants
assert not isinstance(b1, AClass)
b1.spam = 'eggs'
assert isinstance(b1, AClass)  # custom __instancecheck__ now returns True
assert isinstance(c, AClass)   # same, CClass has spam
