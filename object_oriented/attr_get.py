import re


class AClass:
    def __init__(self, s: str):
        self.s = s

    def print_upper(self):
        print(self.s.upper())

    def print_lower(self):
        print(self.s.lower())

    def print_title(self):
        print(self.s.title())

    def print_no_punct(self):
        print(re.sub(r"[.,;!?:-]", " ", self.s))

    def __getattribute__(self, item):
        if item != '__class__':  # Hide multiple debugger request
            print(f"__getattribute__: '{item}'")  # for every attribute access
        return object.__getattribute__(self, item)  # must use object.__getattribute__ to avoid recursion

    def __getattr__(self, item):
        print(f"__getattr__     : '{item}'")  # only when the attr does not exist
        if item in ('upper', 'lower', 'title', 'no_punct'):
            return getattr(self, f'print_{item}')  # will start another attribute lookup!
        raise AttributeError(f"attr {item} not found")


a = AClass("All generaliZatioNs are wrong!\n")
print(a.upper)
print(a.print_upper)
assert a.upper == a.print_upper
assert a.upper is not a.print_upper  # see func_bind.py
print(a.s)
print("\n=====")
a.print_upper()
a.upper()
a.lower()
a.title()
a.no_punct()
try:
    a.foo()
except AttributeError as e:
    print(repr(e))

print("\n===== Magic methods =====")
# Explicit attribute lookup of a magic method.
# Goes through __getattribute__
print("\n----- Explicit magic method call")
# __repr__ is on object.__repr
# AClass *inherits* from object, so __repr__ is found on the attr lookup path (instance a >> AClass >> object)
print(a.__repr__)  # not __getattr__ on the instance
assert '__repr__' not in a.__dict__ and '__repr__' not in AClass.__dict__

# __doc__ is created with the class
print(a.__doc__)  # not __getattr__ on the instance)
assert '__doc__' in AClass.__dict__

try:
    # __name__ belongs to *type*, so it's not reachable from the instance
    # AClass is *an instance* of type, and therefore AClass itself can reach it (it's parent)
    # But it's not reachable for *instance* of AClass
    print(a.__name__)  # fails, goes to __getattr__ for the instance and fails
except Exception as e:
    print(repr(e))

assert '__name__' in type.__dict__
print(type.__name__)
print(AClass.__name__)

# Note: AClass "sees" magic methods both on object (through inheritance) and type (which AClass is an instance of)
# instance of AClass sees only AClass >> object
# see type_object.py, and metaclass

print("\n----- Implicit magic method call")

class BClass:
    def __getattribute__(self, item):
        print("BClass __getattribute__ invoked")
        return object.__getattribute__(self, item)

    def __len__(self):
        return 42

    def say_hi(self):
        return 'hi'


b = BClass()
print(len(b))  # implicit special method lookup: __getattribute__ is bypassed
print(b.__len__())  # explicit
print(b.say_hi())  # common attr, invoke getattribute
