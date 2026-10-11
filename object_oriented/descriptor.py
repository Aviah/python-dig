from random import randrange


class Descriptor42:
    def __get__(self, obj, objtype=None):
        # returns the same str for both instance and class (for demo, not recommended)
        if obj is None:
            print(f"{self} __get__ was invoked from class {objtype}")
        return f"The answer is 42"


class DescriptorRandom:

    def __init__(self):
        self._d = {}

    def __set_name__(self, owner, name):
        """
        Receives the class attr name that was assigned to this descriptor.
        Useful to let the descriptor know the attr it was assigned to and manages
        Or when it mimics common attr behavior, while doing additional work behind the scene
        """
        print(f"{self} __set_name__ invoked: attr {name} of {owner}")
        self.attribute_name = f'_random_{name}'

    def __get__(self, obj, objtype=None):
        if obj is None:
            print(f"{self} __get__ was invoked from class {objtype}")
            return self  # common practice

        if obj not in self._d:
            # A descriptor instance is assigned to an attribute per *class*
            # It can hold value per *instance*
            # Note: demo only, strong ref to every instance is a memory hog. In real code use weakref or other mechanism
            self._d[obj] = randrange(1000)
        return self._d[obj]  # The descriptor returns different value for each instance

print("\n ===== Class access =====")

class AClass:
    answer1 = Descriptor42()
    answer2 = Descriptor42()
    answer3 = DescriptorRandom()
    answer4 = DescriptorRandom()


print(AClass.answer1)
print(AClass.answer2)
assert AClass.answer1 == AClass.answer2  # string
print(AClass.answer3)
print(AClass.answer4)
assert AClass.answer3 is not AClass.answer4  # each class attr gets its own descriptor instance

print("\n ===== Instance access =====")

a = AClass()
print(a.answer1)  # For demo, the descriptor returns string for both class and instance access
print(a.answer2)
print(a.answer3)
print(a.answer4)

a1 = AClass()
print(a1.answer1)
print(a1.answer2)
print(a1.answer3)
print(a1.answer4)


print("-----")

# Same descriptor instance per attr/class holds dedicated value per instance
d = AClass.answer3
assert a in d._d
assert a1 in d._d
assert len(d._d) == 2
print(d)
print(d._d)


print("\n=====")

print(vars(a))
a.answer3 = 4200
print(vars(a))  # Python allows to override non data descriptor, and reassign the attribute
print(a.answer3)
print(a.answer4)  # Still uses the descriptor
del a.__dict__['answer3']
print(a.answer3)  # back to the descriptor

print("\n=====")

print(AClass.answer1)
print(AClass.__dict__['answer1'])
try:
    del AClass.__dict__['answer1']
except TypeError as e:
    print(repr(e))  # Python provides read-only __dict__ for class
del AClass.answer1  # type.__delattr__
try:
    print(AClass.answer1)
except AttributeError as e:
    print(repr(e))

print(AClass.answer3)
print(vars(AClass)['answer3'])
