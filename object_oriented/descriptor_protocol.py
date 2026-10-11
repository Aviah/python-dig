from random import randint


class Descriptor:
    def __set_name__(self, owner, name):
        pass

    def __get__(self, obj, objtype=None):
        return 42


class DataDescriptor1:
    def __init__(self, *args, **kwargs):
        # strong refs to all *class* instances accessed through this *descriptor* instance
        # (this is a bad idea to do in real prod code)
        self._obj_store = {}

    def __set_name__(self, owner, name):
        self._internal_name = f"_attr_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # Invoked from the class

        if obj not in self._obj_store:
            self._obj_store[obj] = randint(0, 1000)
        return self._obj_store[obj]

    # __set__ or __delete__ (or both) makes the descriptor a data descriptor
    def __set__(self, obj, value):
        self._obj_store[obj] = value

    def __delete__(self, obj):
        del self._obj_store[obj]


class DataDescriptor2:
    def __set_name__(self, owner, name):
        pass

    def __get__(self, obj, objtype=None):
        return 42

    # __set__ or __delete__ (or both) makes the descriptor a data descriptor
    def __delete__(self, obj):
        # Just to make this a data descriptor
        raise NotImplementedError


class AClass:
    p1 = Descriptor()
    p2 = DataDescriptor1()
    p3 = DataDescriptor2()
    p4 = DataDescriptor1()


a = AClass()
print(a.p1)
print(a.p2)
print(a.p3)
print(a.p4, a.p4, a.p4)  # value per instance/attr

print("\n=====")

a.p1 = 100
print(vars(a)['p1'])  # No set method, just sets the attribute
print(a.p1)  # instance's __dict__ attr wins a non-data descriptor in the attr lookup
a.p2 = 1234
assert 'p2' not in vars(a)
print(a.p2)  # Data descriptors win, gets the 1234 from its internal storage
try:
    a.p3 = 100
except AttributeError as e:
    print(f"{repr(e)}")  # Data descriptor wins, but it doesn't have a __set__ method


print("\n=====")

a.__dict__['p2'] = 1000
print(vars(a))
print(a.p2)  # Data descriptor wins
delattr(a, 'p2')
print(a.p2)  # The descriptor creates new randint for this instance/attr
delattr(DataDescriptor1, '__set__')
delattr(DataDescriptor1, '__delete__')  # now it's a non-data descriptor
print(a.p2)  # The descriptor is no longer data descriptor, the instance's attr wins


print('\n=====')

print(vars(a))
print(a.p1)  # instance attr wins the non-data descriptor
del a.p1
print(vars(a))
print(a.p1)  # 42. No instance attr, non-data descriptor kicks in


print('\n=====')


class ReadOnlyDataDescriptor:
    """A get read only descriptor, implemented as data descriptor"""

    def __init__(self, x):
        self._x = x

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return self._x

    def __set__(self, obj, value):
        # Has a __set__ method, so it's considered data descriptor
        raise AttributeError("Read Only!")


print("\n===== Read only descriptor =====")

class BClass:
    p1 = ReadOnlyDataDescriptor(42)
    p2 = ReadOnlyDataDescriptor(1234)


b = BClass()
print(b.p1)
print(b.p2)
b.__dict__['p1'] = 9999
print(b.p1)  # data descriptor wins
try:
    b.p1 = 9999  # __setattr__ raises: it's read only
except AttributeError as e:
    print(repr(e))


print("\n===== No __get__ =====")

class NoGetDataDescriptor:
    def __init__(self, attr_name=None):
        self._attr_name = attr_name

    def __set_name__(self, owner, name):
        print(f"{self} __set_name__ invoked: {owner}.{name}")
        if self._attr_name is None:
            self._name = name
        else:
            self._name = self._attr_name

    def __set__(self, instance, value):
        # setattr(instance, self._name, value)  will recurse
        instance.__dict__[self._name] = value


class CClass:
    foo = NoGetDataDescriptor()
    baz = NoGetDataDescriptor()
    callme = NoGetDataDescriptor('_callme')


c1 = CClass()
c1.foo = 'spam'
c1.baz = 'eggs'
c1.callme = 'maybe'
print(vars(c1))  # were set by the descriptor __set__

# No __get__ on the descriptor: reading does not invoke the descriptor
# If the attr exists on the instance, it is returned
print(c1.foo)
print(c1.baz)
print(c1.callme)  # No instance attr named "callme", lookup returns the descriptor *object* from the class
