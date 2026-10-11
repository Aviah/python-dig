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

assert issubclass(BClass, BClass)
assert issubclass(BClass, AClass)
assert issubclass(CClass, BClass)
assert issubclass(CClass, AClass)
assert issubclass(CClass, object)
assert issubclass(CClass, (AClass, BClass, DClass))  # is subclass of any in the tuple (not all)
assert issubclass(EClass, (DClass, CClass, BClass, AClass, object))


print("\n-----")
class AnotherClass(AClass):
    pass

print(AClass.__subclasses__())  # Only the direct subclasses
print(EClass.__bases__)
print(AClass.__class__) # instance of type
assert type(AClass) == AClass.__class__
print(EClass.__class__) # instance of type, subclass DClass,EClass

print("\n===== Init subclass =====")
# A lightweight mechanism to handle subclass initialization, without a custom metaclass

class Pasta:
    base = None

    def __init_subclass__(cls, /, **kwargs):
        print(f"__init_subclass__ invoked: {cls}")
        base = kwargs.pop('base', None)
        super().__init_subclass__(**kwargs)
        cls.base = base

class TomatoesPasta(Pasta, base="tomatoes"):  # Also allows to provide kwargs with the class declaration
    ...

class OliveOilPasta(Pasta, base='olive-oil'):
    ...


print(TomatoesPasta.base)
print(OliveOilPasta.base)