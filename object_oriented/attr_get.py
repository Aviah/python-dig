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
        print(re.sub('[\.\,\;\!\?\:\-]', " ", self.s))

    def __getattribute__(self, item):
        print(f"__getattribute__ called for '{item}'")  # for every attribute access
        return object.__getattribute__(self, item)  # must use object.__getattribute__ to avoid recursion

    def __getattr__(self, item):
        print(f"__getattr__ called for '{item}'")  # only when the attr does not exist
        if item in ('upper', 'lower', 'title', 'no_punct'):
            return getattr(self, f'print_{item}')
        raise AttributeError(f"attr {item} not found")


a = AClass("<All generaliZatioNs - are wrong!>\n")
print(a.upper)
print(a.print_upper)
assert a.upper == a.print_upper
print(a.s)
print("=====")
a.print_upper()
a.upper()
a.lower()
a.title()
a.no_punct()
try:
    a.foo()
except AttributeError as e:
    print(repr(e))
print("=====")
print(a.__repr__)
print(a.__doc__)
try:
    print(a.__name__)  # fails after lookup
except Exception as e:
    print(repr(e))
print("=====")


class BClass:
    def __getattribute__(self, item):
        print("BClass __getattribute__ invoked")
        return object.__getattribute__(self, item)

    def __len__(self):
        return 42

    def say_hi(self):
        return 'hi'


b = BClass()
print(len(b))  # explicit special method, getattribute skipped
print(b.say_hi())  # common attr, invoke getattribute
