"""
@classmethod
class namespace (__dict__): classmethod descriptors
class: The descriptor returns bound method with *class* as __self__ (the common practice is to call this arg cls)
instance: Gets to the class-bound method via attr lookup

@staticmethod
class namespace (__dict__): staticmethod descriptors
class: The descriptor returns the plain function
instance: Finds the descriptor on the class

Common method
class namespace (__dict__): the function object (has __get__, acts as descriptor)
class: The function-object-as-descriptor returns the plain function
instance: The function-object-as-descriptor returns bound method to instance

Important: Descriptor behavior is triggered when the descriptor is found on the class/MRO

Note: "Bound to" is what is stored on the method object __self__
Essentially, the descriptor returns a method object with __self__ and __funct__,
and Python calls m.__func__(m.__self__,...)
For classmethod, __self__ is the class, for common methods, __self__ is the instance
staticmethod does not need __self__

Note:
Since 3.13 Python doesn't support wrapping @property
This will not work:
@classmethod
@property
def foo(self)
    ...

The reason is that @property is *also* a descriptor, so wrapping it @classmethod considered a design flaw,
that caused wrong behavior down the road.
"""

class Foo:
    @classmethod
    def class_m(cls):
        print(f"I am class {cls}")

    @staticmethod
    def static_m(x):
        return x * 2

    def common_m(self):
        print(f"I am instance {self}")


class Baz:
    pass

print("\n===== Meet the descriptors =====")
print(Foo.__dict__['class_m'])
print (Foo.__dict__['static_m'])
print (Foo.__dict__['common_m'])


print(type(Foo.class_m))
print(type(Foo.static_m))
print(type(Foo.common_m))


print("\n=====")

f1 = Foo()
f2 = Foo()
# @classmethod descriptor replaced the function, and returns a method that is bound to the *class*
Foo.__dict__['class_m'].__get__(None, Foo)()
Foo.__dict__['class_m'].__get__(None, Baz)()  # actual classmethod descriptor: binds cls to Baz
Foo.class_m.__get__(None, Baz)()  # Foo.class_m triggered lookup and descriptor call, it's already Foo
print(Foo.class_m.__self__)  #  The @classmethod descriptor returned a bound method for the *class*
print(Foo.class_m.__func__)
Foo.class_m.__get__(f1, Foo)()  # already-bound method stays bound to Foo

# Call simple method: the descriptor returns instance-bound function
assert not hasattr(Foo.common_m, '__self__')  # This is the function descriptor itself
assert not hasattr(Foo.common_m, '__func__')
assert hasattr(f1.common_m, '__self__')  #  This is the bound function, from the instance
assert hasattr(f1.common_m, '__func__')
Foo.common_m.__get__(Foo)()  # Passes the *class* as the *instance, works (normally it's None,Foo for the class)
Foo.common_m.__get__(Baz)()
Foo.common_m.__get__(f1)()
Foo.common_m.__get__(f2)()

print("\n=====")
assert Foo.common_m is Foo.common_m  # *class* access, the descriptor returns the same function object stored for the class
assert Foo.common_m is not f1.common_m  # plain function vs the instance-bound method
assert f1.common_m is not f1.common_m  # new bound method is returned by the descriptor on each call
assert Foo.class_m is not Foo.class_m  # @classmethod descriptor return new bound method on the *class*
assert f1.class_m is not f1.class_m
assert Foo.class_m is not f1.class_m
assert Foo.static_m is f1.static_m  # static function, same, the @staticmethod descriptor returns it as is
assert f1.static_m is f1.static_m

print("\n==== Non data descriptors =====")
# The method descriptors are non data descriptors (only __get__), and the instance can override them
f1.class_m = 100
f1.static_m = 200
f1.common_m = 300
print(f1.class_m, f1.static_m, f1.common_m)


#  History: http://python-history.blogspot.com/2009/02/first-class-everything.html
