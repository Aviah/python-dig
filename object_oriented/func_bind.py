# This isn't super helpful, but it's cool to see how function objects and descriptors work
# Function objects are non-data descriptors that have a __get__ method
# When used outside an instance, the descriptor just returns the function
def f(x):
    return x + 100


print(f)
print(f.__get__)
print(f.__get__(1000)())
f1 = f.__get__(42)
print(f1)  # By the descriptor, "bound" to an arg
print(f1())  # Already got 42 as x. This is how an object's method gets to the "self" argument
print(f1.__func__)  # Ref to the original func
assert f1.__func__ is f
print(type(f))
print(type(f1))  # Even though we didn't use "f" in a class

# The real job of function's __get__ is to bind it to an instance and make it a method. See object_oriented
# History: http://python-history.blogspot.com/2009/02/first-class-everything.html
# Descriptor wrappers: https://discuss.python.org/t/difference-between-slot-wrapper-method-wrapper-and-wrapper-descriptor/14184/5
# Documentation: https://docs.python.org/3/howto/descriptor.html#functions-and-methods
