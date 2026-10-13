class AClass:
    __slots__ = ('country', 'lang')


class MoreSlots(AClass):
    # Still has access to its parent's slots
    __slots__ = ('city',)


class BClass(AClass):
    # Still has access to its parent slots
    # Yet because no __slots__ in it's own definition, allows instances' __dict__ and ordinary attrs
    pass


m = MoreSlots()
print(m.__slots__)
assert not hasattr(m, '__dict__')
try:
    m.foo = 'bar'
except AttributeError as e:
    print(repr(e))
m.country = 'Never-never land'  # works! Still access to parent's slots
print(m.country)

print("\n----- Actual MoreSlots slots:")

for cls in MoreSlots.__mro__:
    if '__slots__' in cls.__dict__:
        for slot in cls.__slots__:
            print(f"{slot} from {cls.__name__}")


print("\n===== Mixed slots and ordinary attrs")
# Through subclassing, Pythons allows mixed instances: with both __dict__ and __slots__

b = BClass()
print(b.__slots__)
print(b.__dict__)  #  Subclassed __slots__, but not a __slots__ only class, so has both
b.bar = 'baz'
print(b.__dict__)
print(b.bar)  # ordinary attr
print(type(AClass.country))
b.country = 'Balnibarbi'  # managed by the slots descriptor
print(b.__dict__)


print("\n-----")

class CClass(AClass):
    country = 'Luggnagg'  # subclass can override a slot

print(type(CClass.country))
print(b.__slots__)  # inherited AClass.__slots__; BClass itself declares no slots
print(CClass.__slots__)  # same: inherited attribute, not CClass's own slot declaration
print(CClass.__dict__['country'])
c = CClass()
print(c.__slots__)
print(c.__dict__)
c.spam = 'eggs'
c.lang = 'English'
print(c.lang)  # slot
print(c.spam)  # ordinary instance attr
print(c.country)  # Class attr: found in the attr lookup before it reaches the parent country slot
AClass.country.__set__(c, 'Laputa')  # slot descriptor
print(AClass.country.__get__(c, AClass))  # Laputa, slot descriptor
print(c.country)  # Luggnagg, ordinary lookup, shadows the descriptor protocol