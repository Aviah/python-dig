class AClass:
    spam = 'eggs'


class BClass(AClass):
    foo = 'baz'


print("\n===== type =====")
print(type.__getattribute__(AClass, 'spam'))
print(BClass.__bases__)
print(type.__getattribute__(BClass, 'spam'))  # type do class lookup, and goes to the bases
print(type.__getattribute__(BClass, 'foo'))

try:
    print(type.__getattribute__(AClass(), 'spam'))
except TypeError as e:
    print(repr(e))


print("\n===== object =====")
print(object.__getattribute__(AClass(), 'spam'))
print(BClass.__mro__)
print(object.__getattribute__(BClass(), 'spam'))


print("=====")
print(object.__getattribute__(AClass, 'spam'))
print(object.__getattribute__(BClass, 'foo'))
print(type(BClass))
assert not hasattr(type(BClass), 'spam')
print(object.__getattribute__(BClass, 'spam'))  # fails, see metaclass_attr.py
