class AClass:
    ...

print("\n===== Truthiness =====")

# False
print(bool(''))
print(bool(0))
print(bool([]))
print(bool(set()))
print(bool({}))


print("\n-----")

# True
print(bool("a"))
print(bool(-1))
print(bool([1, 2, 3]))
print(bool({1, 2, 3}))
print(bool({'foo': 'baz'}))
print(bool(AClass))
print(bool(AClass()))


print("\n=====")

s1 = ""
s2 = "Laputa"
s3 = "Glubbdubdrib"


if s1 and s2 and s3:
    print("Success")

# No NameError
# Python short circuits, will not evaluate undefined x, y after failed predicate
if s1 and x and y:
    print("Success")
else:
    print("Fail")

# all/any are more convenient to pack many predicates
try:
    if all([s1, x, y]):
        print("Success")
    else:
        print("Fail")
except NameError as e:
    print(repr(e))  # all and any also short circuit, but the list arguments are evaluated before all() is called

def check(name, result):
    print (f"Checking {name}...")
    return result

print(all(
    check(name, result)
    for name, result in [
        ("Brobdingnag", True),
        ("Laputa", False),
        ("Will not get here", True),  # lazy evaluation: Laputa fails, not running this
    ]
))


if any([s1, s2, s3]):
    print("Success")
else:
    print("Fail")

result = "Great" if len(s3) > len(s2) else "Not so great"  # conditional expression
print(result)


print("\n===== Multiple conditions =====")

if s1:
    print(s1)
elif len(s2) > len(s3):
    print(s2)
elif s3 == 'Luggnagg':
    print(s3)
else:
    print("Utopia")

# for structured multiple matching see patterns_match.py


print("\n===== In comprehensions =====")
# Similar to filter

print([x for x in range(100) if x % 5 == 0])
print([x for x in ['foo', 1, 'baz', 2, 'spam', 3, 'eggs', 4] if (len(x) > 3 if isinstance(x, str) else x>=3)])


print("\n===== Customise truthiness =====")
# Truth-value testing: __bool__() if defined, otherwise __len__() if defined, otherwise the object is truthy
# __bool__ must return bool; __len__ must return a non-negative integer.

class BClass:
    def __bool__(self):
        return False

class CClass:
    def __len__(self):
        return 0

assert not BClass()
assert not CClass()
if not BClass() and not CClass():
    print("Fail")  # Falsy objects


class DClass:
    ...

assert '__bool__' not in dir(DClass())
assert '__len__' not in dir(DClass())
assert DClass()  # no __bool__ or __len__, so truthy by default