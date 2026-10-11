""" This is confusing, "type" and "object"
Python separates the machinery to create and handle object-oriented parts to:
* instance handling with "object"
* classes handling with "type"
* Python provides clear separation between the two

The idea is to remove most differences between builtin types and user defined types, so to allow subtype builtin type
and unified types and classes system.
See: https://www.python.org/download/releases/2.2.3/descrintro/

However, this creates some circular confusing relations between the two "buckets" of type and object, since both
need functionality that the other provides.

Structure:
* object is *instance* oriented, provides the capabilities of common instances
* type is *class* oriented, provides the machinery to create, inherit and use classes
* Each contains magic methods that are required to do it's job: object for instances, type for class

The confusing part:
* type is actually the direct class of type: type(type)
* So type is an instance of type (type builtin works on itself)
* type is also a subclass of object. It inherits from object
* Now the scary part: type is an instance of type, where type is a subclass of object, so via inheritance:
type is an instance of object (it's actual class is a subclass of object)
* The circular part: the type of object is type: object is an instance of type


Inheritance:
type >> object
class >> object

Instance-of:
instance >> class
class >> type (since type(class) is type)
type >> type
object >> type

So we can think of "object" as a general instance bucket of tools, and type as more specific bucket for classes.
Both use each other

Class lookup:
* Class is a subclass of object: has it's magic methods
* Class is an instance of type (or of a custom type: subtype of builtin type or a custom metaclass that is a subtype of type)
* So for classes, object appears in two places above it: as a superclass, and as the parent of it's type
* Class lookup will search both (see class_attr_lookup.py)
* type itself is a metaclass

Instance lookup:
* Instance is an instance of it's class
* So object is on the end of an instance lookup path (which provide all instance capabilities)
* Lookup check the instance and then MRO along the inheritance path up parent classes, with object at it's end
* The *instance's* type is it's *direct* class. So instance does not have access to it's class's type
* Can not access type attrs (which the class itself can)

Some "object" magic methods: baseline object/instance behavior

object.__new__
object.__init__
object.__getattribute__
object.__setattr__
object.__delattr__
object.__repr__
object.__str__
object.__eq__
object.__ne__
object.__hash__
object.__format__
object.__sizeof__

Some "type" magic methods: Python's class-object machinery

type.__new__       # creates class objects
type.__init__      # initialization of class objects
type.__call__      # handles calling class objects, e.g. A()
type.__getattribute__
type.__setattr__
type.__delattr__
type.__repr__      # representation for class objects
type.__instancecheck__
type.__subclasscheck__
type.__prepare__


Note:
__call__ is a good example why Python separates the "master object" to type and object:
* Python puts __call__ on type: that makes the class callable.
* It could put __call__ on object, and class would still get it
* But then, also instances would be callable, and this is not how Python is designed


"""

assert type(type) is type
assert issubclass(type, object)
assert isinstance(type, object)  #  # type(type) is type, and type is a subclass of object

assert type(object) is type
assert isinstance(object, type)

# The circular relationship
assert isinstance(object, object)
assert isinstance(type, type)

print("\n=====")

two = 2
print(type(two))
print(dir(two)[:10])
print(vars(type(two))['__repr__'])

print("\n=====")
print(object)
print(object.__class__)
print(object.__bases__)
print(object.__mro__)

print("=====")
print(type)
print(type.__class__)
print(type.__bases__)
print(type.__mro__)
assert issubclass(type, object)

print("=====")


class AClass:
    pass


assert isinstance(AClass, type)
assert type(AClass) is type
assert isinstance(AClass(), object)
assert type(AClass()) is AClass
assert not isinstance(AClass, AClass)
assert not isinstance(list, list)
assert isinstance(type, type)
assert isinstance(object, object)
assert isinstance(type, object)
assert isinstance(object, type)
print(AClass)
print(AClass.__class__)
print(AClass.__bases__)
print(type.__class__)
print(object.__class__)
print("=====")
print(list)
print(type(list))
print(list.__class__)
print(list.__bases__)
print(list.__mro__)

print("=====")
# primitive objects
try:
    type.__new__ = lambda x: x
except TypeError as e:
    print(repr(e))

try:
    object.__new__ = lambda x: x
except TypeError as e:
    print(repr(e))
