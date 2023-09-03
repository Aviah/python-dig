class AClass:
    def __init__(self):
        print(f"__init__ got: {self}")  # instance

    def __new__(cls, *args, **kwargs):
        print(f"__new__ got: {cls}")  # class
        return super().__new__(cls, *args, **kwargs)


a = AClass()
assert a.__init__ is not AClass.__init__
assert a.__new__ is AClass.__new__  # Python considers __new__ static w/o the decorator
