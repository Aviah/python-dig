class AClass:
    pass


class BClass(AClass):
    pass


class CClass(BClass):
    pass


class DClass:
    pass


class EClass(DClass, CClass):
    pass


assert issubclass(BClass, AClass)
assert issubclass(CClass, BClass)
assert issubclass(CClass, AClass)
assert issubclass(CClass, object)
assert issubclass(CClass, (AClass, BClass, DClass))
assert issubclass(EClass, (DClass, CClass, BClass, AClass, object))
print(EClass.__bases__)
