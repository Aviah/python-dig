"""
This isn't super helpful, but it's cool to see how function objects and descriptors work
Function objects are non-data descriptors: they implement a __get__, but not __set__ or __delete__
When used in classes, they work as ordinary methods, see method_descriptors.py
When __get__ is called with obj=None, it returns the plain function.
When called with an object, it binds the function to that object and returns a bound method.
The real job of function's __get__ is to bind it to an instance and make it a method
"""

def f(x):
    return x + 100


print(f)
print(f.__get__)
print(f.__get__(1000)())
f1 = f.__get__(42)
print(f1)  # Returned by the descriptor, "bound" to an arg, here it's 42
print(f1())  # Works! already got 42 as x, so effectively f(42). This is how an object's method gets the "self" argument
print(f1.__func__)  # Ref to the plain func
assert f1.__func__ is f
print(type(f))
print(type(f1))  # Even though we didn't use "f" in a class, "bound" is considered "method"

