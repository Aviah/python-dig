class AClass:
    __slots__ = 'country'


class MoreSlots(AClass):
    __slots__ = 'city'


class BClass(AClass):
    pass  # no slots


m = MoreSlots()
print(m.__slots__)
assert not hasattr(m, '__dict__')
m.country = 'Never never land'
print(m.country)

print("=====")
b = BClass()
print(b.__slots__)
print(b.__dict__)  # from s subclass, has both
b.bar = 'baz'
print(b.__dict__)
print(b.bar)

print("=====")
print(type(AClass.country))
b.country = 'Balnibarbi'
print(b.__dict__)

print("=====")


class CClass(AClass):
    country = 'Luggnagg'


print(type(CClass.country))
print(CClass.__slots__)
print(CClass.__dict__)
c = CClass()
print(c.__slots__)
print(c.__dict__)
print(c.country)  # from the slot
