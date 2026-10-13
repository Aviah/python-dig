class AClass:
    __slots__ = ('foo', 'baz')
    spam = 42

# Class is allowed to add attrs outside slots  (it has a __dict__), as long as they don't collide with a slot
# Instance can't add ordinary attrs, it will not get a __dict__
print(AClass.spam)
assert 'spam' in AClass.__dict__
a = AClass()
print(a.spam)

try:
    a.pool = 42
except AttributeError as e:
    print(repr(e))

try:
    class BClass:
        __slots__ = ('spam', 'eggs')
        spam = 42  # Conflicts with a slot
except ValueError as e:
    print(repr(e))