from random import randrange


class Descriptor42:
    def __get__(self, obj, objtype=None):
        # returns the same str for both instance and class (for demo, not recommended)
        return "The answer is 42"


class DescriptorRandom:
    _d = {}

    def __set_name__(self, owner, name):
        """
        Get the class property name that was assigned to this descriptor.
        Useful to let the descriptor edit properties on the object itself
        See data_descriptor.py
        """
        self.attribute_name = f'_random_{name}'

    def __get__(self, obj, objtype=None):
        if obj is None:
            print("Invoked from class")
            return self  # common practice

        if obj not in self._d:
            self._d[obj] = randrange(1000)
        return self._d[obj]


class AClass:
    answer1 = Descriptor42()
    answer2 = Descriptor42()
    answer3 = DescriptorRandom()
    answer4 = DescriptorRandom()


print(AClass.answer1)
print(AClass.answer2)
assert AClass.answer1 is AClass.answer2
print(AClass.answer3)
print("=====")


a = AClass()
print(a.answer1)
print(a.answer2)
print(a.answer3)
print(a.answer4)
a1 = AClass()
print(a1.answer1)
print(a1.answer2)
print(a1.answer3)
print(a1.answer4)
assert a.answer3 is not a1.answer3
print("=====")

print(vars(a))
a.answer3 = 4200
print(vars(a))  # Python allows to override non data descriptor, and reassign the attribute
print(a.answer3)
print(a.answer4)  # Still uses the descriptor
del a.__dict__['answer3']
print(a.answer3)  # back to the descriptor

print("=====")
print(AClass.answer1)
print(AClass.__dict__['answer1'])
print(AClass.answer3)
print(vars(AClass)['answer3'])
