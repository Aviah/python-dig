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
    print(type.__getattribute__(AClass(), 'spam'))  # type expects a class, not instance
except TypeError as e:
    print(repr(e))


print("\n===== object =====")

print(object.__getattribute__(AClass(), 'spam'))
print(BClass.__mro__)
print(object.__getattribute__(BClass(), 'spam'))


print("\n=====")

assert 'spam' in AClass.__dict__
assert  'foo' in BClass.__dict__
print(object.__getattribute__(AClass, 'spam'))  # AClass is also an object, so *direct* attr works
print(object.__getattribute__(BClass, 'foo'))

print("\n-----")
print(type(BClass))
assert not hasattr(type(BClass), 'spam')
# fails
# object's __getattribute__ uses ordinary instance lookup
# instance's __dict__ + type(object) mro.
# Here the object is BClass
#   - "spam" is not in BClass __dict__
#   - And for mro: BClass type it type, which does not have attr "spam"
try:
    object.__getattribute__(BClass, 'spam')
except AttributeError as e:
    # Python keeps clear separation between instance lookup and class based lookup
    print(repr(e))
