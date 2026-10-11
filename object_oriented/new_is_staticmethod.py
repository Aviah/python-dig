"""
__new__ runs *before* the instance exists, so there nothing to bind with - must be static
"""
class AClass:
    def __init__(self):
        print(f"__init__ got: {self}")  # instance

    def __new__(cls, *args, **kwargs):
        print(f"__new__ got: {cls}")  # class
        return super().__new__(cls)


a = AClass()
assert a.__init__ is not AClass.__init__
assert a.__new__ is AClass.__new__  # Python considers __new__ staticmethod w/o the decorator
