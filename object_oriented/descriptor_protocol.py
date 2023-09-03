from random import randint


class Descriptor:
    def __set_name__(self, owner, name):
        pass

    def __get__(self, obj, objtype=None):
        return 42


class DataDescriptor1:
    def __init__(self, *args, **kwargs):
        self._obj_store = {}

    def __set_name__(self, owner, name):
        self._name = f"_private_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self  # Invoked from the class

        if obj not in self._obj_store:
            self._obj_store[obj] = randint(0, 1000)
        return self._obj_store[obj]

    # __set__ or __delete__ (or both) makes the descriptor a data descriptor
    def __set__(self, obj, value):
        if value:
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
        # Do something, typically delete an object attr
        pass


class AClass:
    p1 = Descriptor()
    p2 = DataDescriptor1()
    p3 = DataDescriptor2()


print(AClass.p2)

a = AClass()
print(a.p1)
print(a.p2)
print(a.p3)

a.p1 = 100
print(vars(a)['p1'])  # No set method, just sets the attribute
print(a.p1)  # instance's __dict__ attr before non-data descriptor in the attr search
a.p2 = 1234
assert 'p2' not in vars(a)  # But not for data descriptors, goes to the __set__ method
try:
    a.p3 = 100
except Exception as e:
    print(f"Exception: {repr(e)}")  # No set method


print('=====')
a.__dict__['p2'] = 1000
print(vars(a))
print(a.p2)  # Data descriptor takes precedence
delattr(a, 'p2')
print(a.p2)  # new randint
delattr(DataDescriptor1, '__set__')
delattr(DataDescriptor1, '__delete__')  # now it's a non-data descriptor
print(a.p2)  # the instance's attr
print('=====')
print(vars(a))
print(a.p1)
del a.p1
print(vars(a))
print(a.p1)  # No attr, so use the descriptor


class ReadOnlyDataDescriptor:
    """A get read only descriptor, implemented as data descriptor"""

    def __init__(self, x):
        self._x = x

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        return self._x

    def __set__(self, obj, value):
        # Has a __set__ method, so it's considered data descriptor
        raise ValueError("Read Only!")


print("=====")


class BClass:
    p1 = ReadOnlyDataDescriptor(42)
    p2 = ReadOnlyDataDescriptor(1234)


b = BClass()
print(b.p1)
print(b.p2)
b.__dict__['p1'] = 9999
print(b.p1)
try:
    b.p1 = 9999
except ValueError as e:
    print(repr(e))


print("=====")


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
print(vars(c1))
# The descriptor for has no __get__, Python uses it's default __get__
print(c1.foo)  # Same name, so get the attr from __dict__
print(c1.baz)
print(c1.callme)  # the attr is _callme, Python default __get__ returns the descriptor
