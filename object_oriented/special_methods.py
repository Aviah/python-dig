# dunder methods
class AClass:
    def __call__(self, *args, **kwargs):
        print(self)
        print("Awesome!")


a = AClass()
a()


def print_great(self=None):
    print(self)
    print("Great!")


a.__call__ = print_great
print(vars(a))
a()
a.__dict__['__call__'].__get__(a)()
a.__dict__['__call__']()
AClass.__call__.__get__(a)()
AClass()  # calls the metaclass __call__ (same idea, but with class/metaclass)


print("=====")
a1 = AClass()
assert '__len__' not in dir(a1)
a1.__len__ = lambda: 5  # do nothing
print(a1.__dict__)
assert '__len__' in dir(a1)
try:
    print(type(a1))
    len(a1)
except TypeError as e:
    print(repr(e))  # not defined on the type


class BClass:
    def __len__(self):
        return 5


b = BClass()
print(type(b))
print(len(b))
