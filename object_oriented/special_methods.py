# dunder methods
class AClass:
    def __call__(self, *args, **kwargs):
        print(f"{self} __call__ invoked")
        print("Awesome!")


a = AClass()
a()


def print_great(self=None):
    print(self)
    print("Great!")


a.__call__ = print_great  # instance, does not affect class real magic method
print(vars(a))
a()  # Implicit magic method call. Python looks for the magic method directly on the class
a.__dict__['__call__'].__get__(a)()  # We call the instance's function
a.__dict__['__call__']()  # instance
a.__dict__['whatever'] = print_great
a.__dict__['whatever']()  # ordinary callable instance attr

# Conceptually close to what Python runs for magic method call
# (although Python uses special optimized access to magic methods)
AClass.__call__.__get__(a)()

# Class is an object: So Python looks for magic method directly on *its* class - the metaclass (normally type)
# Same idea: conceptually type.__call__.__get__(AClass, type),
# although Python has optimized version to call magic methods (using slots)
AClass()


print("\n=====")
a1 = AClass()
assert '__len__' not in dir(a1)
a1.__len__ = lambda: 5  # do nothing
print(a1.__dict__)
assert '__len__' in dir(a1)  # again, __len__ is a just an ordinary instance attr, len() ignores it
try:
    print(type(a1))
    len(a1)  # Python "formal" magic method call, the instance __len__ attr is ignored
except TypeError as e:
    print(repr(e))  # not defined on the type


class BClass:
    def __len__(self):
        return 5


b = BClass()
print(type(b))
print(len(b))  # Implicit call to the proper magic method on class
