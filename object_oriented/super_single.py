class AClass:
    def __new__(cls, *args, **kwargs):
        print(f"AClass __new__ invoked: {cls} | {args} | {kwargs}")
        assert super().__new__ is object.__new__  # see type_object.py
        return super().__new__(cls)


class BClass(AClass):
    def __new__(cls, *args, **kwargs):
        print(f"BClass __new__ invoked: {cls} | {args} | {kwargs}")
        return super().__new__(cls)


print("=====")
a = AClass()
print(a)
print(type(a).__mro__)
print("=====")
b = BClass()
print(b)
print(type(b).__mro__)
