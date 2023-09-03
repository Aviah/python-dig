class Metaclass(type):
    def __instancecheck__(self, instance):
        print(f"__instancecheck__ invoked: {self, instance}")
        return hasattr(instance, 'spam')


class AClass(metaclass=Metaclass):
    pass


class BClass:
    pass


class CClass:
    spam = 'bar'


a = AClass()
b1 = BClass()
b2 = BClass()
b2.spam = 'eggs'
c = CClass()

assert isinstance(a, AClass)  # not invoked
assert not isinstance(b1, AClass)
assert isinstance(b2, AClass)
assert isinstance(c, AClass)
