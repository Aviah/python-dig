"""
Python's attr lookup mental model


# TL;DR

instance:
    ordinary lookup → instance namespace + class MRO
    special methods lookup  → class MRO

class object:
    ordinary lookup → class MRO + metaclass MRO
    special method lookup  → metaclass MRO


# Detailed

1. An instance's has *one* lookup path:
    - Starts with itself, the instance __dict__ (subject to descriptor precedence)
    - Continue to its direct class __mro__ which is: type(instance).__mro__.
    - Note: the __mro__ begins with the instance direct class
    - Normally this path ends in "object".

2. So ordinary instance attribute lookup considers instance.__dict__, type(instance), type(instance).__mro__
   with descriptor precedence (data descriptors may tell Python to skip instance.__dict__)
Note: type(instance) is the first item on type(instance).__mro__

3. Implicit special-method lookup on an instance skips instance.__dict__. It starts directly at
   type(instance).__mro__. It therefore commonly reaches "object", but any class in the mro can "hijack" the
   special method.

4. Unlike instance, a class object participates in *two* hierarchies:
   - Its own class mro (normal subclassing hierarchy, it's a class, so unlike instance it has __mro__)
   - its metaclass mro (metaclass hierarchy, this is the second look path available only for classes)

5. Ordinary class attribute lookup considers *both* paths:
   Conceptually it looks for metaclass data descriptors → class mro → metaclass attributes.

6. Implicit special-method lookup on a class uses *only* the 2nd path, the metaclass mro:
   - type(Class).__mro__: gets the class's metaclass (not the normal subclassing)
   - Unless customized, this is usually type.
   - For the default metaclass mro, it contains type → object. So normally class special method will
   get to type.__specialmethod__.

   - If type does not define it, lookup may continue to object, if object defines it.
   Note: so some magic method are used from object to both classes and instances.
   - Any metaclass on the mro (again, the *second* mro) can "hijack" a special method before it gets to type/object

7. This is why an ordinary instance cannot see attributes that exist only on its class's metaclass. The metaclass
based lookup path is available only to classes.
"""

# Classes are an *instance* of the metaclass, so attr lookup from class continues to the metaclass
# But not for the class instance
class Metaclass(type):
    foo = 'baz'


class AClass(metaclass=Metaclass):
    pass


class Subclass(AClass):
    pass

assert type(AClass) is Metaclass
assert type(Subclass) is Metaclass

a = AClass()
s = Subclass()
assert hasattr(AClass, 'foo')  # AClass is an *instance* of the metaclass, declared with the `metaclass=` arg: ok
assert hasattr(Subclass, 'foo')  # Subclass is an instance of the metaclass, so lookup can reach foo
assert not hasattr(a, 'foo')  # 'a' is an *instance of an instance* of the metaclass: attr lookup stops at Aclass
assert not hasattr(s, 'foo')  # same

print(f"Lookup path: {a}: {a}, {type(a).__mro__}")
print(f"Lookup path: {s}: {s}, {type(s).__mro__}")
print(f"Lookup path: {AClass}: {AClass}, {type(AClass).__mro__}")
print(f"Lookup path: {Subclass}: {Subclass}, {type(Subclass).__mro__}")


print("\n===== Special method lookup =====")
class Metaclass1(type):

    def __repr__(cls, *args, **kwargs):
        return f"Metaclass1 __repr__ invoked for {cls.__name__}"

class BClass(metaclass=Metaclass1):

    def __repr__(self, *args, **kwargs):
        return f"BClass __repr__ invoked"


class CClass(BClass):
    ...

class Subclass1(CClass):
    ...

# Implicit magic method call
print(repr(Subclass1()))  # instance, common subclassing based mro attr lookup
print(repr(CClass()))  # instance, common subclassing based mro attr lookup
print(repr(CClass))  # class, metaclass based mro lookup: **goes to metaclass**

# Get attribute, Python doesn't invoke the special method mechanism
# Searches the attr in the common subclassing mro
print(getattr(CClass, '__repr__'))
print(getattr(BClass, '__repr__'))
assert getattr(CClass, '__repr__') is getattr(BClass, '__repr__')


print("\n===== Attr access =====")

class Metaclass2(type):
    meta_attr = 'baz'

    def __init__(cls, name, bases, attrs):
        print(f"Metaclass2 __init__ invoked {cls}")
        print(attrs)  # 'foo' will not be provided on e = Eclass()
        print(f"foo in attrs: {'foo' in attrs}")  # Only for DClass
        print(hasattr(cls, 'foo'))
        super().__init__(name, bases, attrs)


class DClass(metaclass=Metaclass2):
    foo = 'baz'


class AnotherSubclass(DClass):
    pass  # will call the metaclass, but w/o foo


class EClass(metaclass=Metaclass2):
    def __init__(self, foo):  # __init__ is an attribute
        self.foo = foo

print("\n----- Class attr lookup")

print(DClass.foo)  # own attr
print(vars(DClass)['foo'])  # own attr
print(AnotherSubclass.foo)  # mro, subclassing
assert hasattr(Metaclass2, 'meta_attr')
# instances of Metaclass
assert isinstance(DClass, Metaclass2)
assert hasattr(DClass, 'meta_attr')
assert isinstance(AnotherSubclass, Metaclass2)
assert hasattr(AnotherSubclass, 'meta_attr')
assert issubclass(AnotherSubclass, DClass)
assert isinstance(EClass, Metaclass2)
assert hasattr(EClass, 'meta_attr')


print("\n----- Instance attr lookup")

d = DClass()
subc = AnotherSubclass()
e = EClass(42)
print(d.foo)  # instance lookup path: subclassing
assert 'foo' not in d.__dict__
print(subc.foo)# instance lookup path: subclassing
assert 'foo' not in subc.__dict__
print(e.foo)  # instance lookup path: instance attr
assert 'foo' in e.__dict__
assert not hasattr(d, 'meta_attr')
assert not hasattr(subc, 'meta_attr')
assert isinstance(subc, AnotherSubclass)
