import weakref

class AClass:
    pass

a = AClass()
awkrf1 = weakref.ref(a)
awkrf2 = weakref.ref(a)
print(awkrf1)
print(awkrf2)
print(AClass.__weakref__)  # descriptor
print(a.__weakref__)  # weakrefs to instance


class BClass:
    __slots__ = ('foo', 'baz')

b = BClass()
try:
    weakref.ref(b)
except TypeError as e:
    print(repr(e))  # no __weakref__ slot, and no __dict__, so BClass instances cannot be weak-referenced


class CClass:
    __slots__ = ('spam', 'eggs', '__weakref__')

c = CClass()
cwkrf = weakref.ref(c)
print(cwkrf)  #  works, there is a slot for __weakref__
