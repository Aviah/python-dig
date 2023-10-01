# Coding super in python from https://www.python.org/download/releases/2.2/descrintro/#cooperation
class Super(object):
    def __init__(self, type, obj=None):
        self.__type__ = type
        self.__obj__ = obj

    def __getattr__(self, attr):
        print("-----")
        if isinstance(self.__obj__, self.__type__):
            starttype = self.__obj__.__class__
        else:
            print("Super from class!")
            starttype = self.__obj__
        print(f"obj: {self.__obj__} | type: {self.__type__}")
        print(f"starttype is {starttype}")
        mro = iter(starttype.__mro__)
        print(f"looping over {starttype.__mro__}")
        for cls in mro:
            print(f"skipping {cls}, done in prev. super calls")
            if cls is self.__type__:
                break
        # Note: mro is an iterator, so the second loop
        # picks up where the first one left off!
        # Now search the attr
        for cls in mro:
            if attr in cls.__dict__:
                x = cls.__dict__[attr]
                if hasattr(x, "__get__"):
                    x = x.__get__(self.__obj__)
                return x
        raise (AttributeError, attr)


class A(object):
    def m(self):
        print(f"A invoked: self is {self}")
        return "A"


class B(A):
    def m(self):
        print(f"B invoked: self is {self}")
        return "B" + Super(B, self).m()


class C(A):
    def m(self):
        print(f"C invoked: self is {self}")
        return "C" + Super(C, self).m()


class D(C, B):
    def m(self):
        print(f"D invoked: self is {self}")
        return "D" + Super(D, self).m()


result = D().m()  # "DCBA"
print("-----")
print(result)
print("=====")
result = C().m()
print("-----")
print(result)
print("=====")
# From the class, we need to specify the obj, which is the class
# Which is why you have to code super(cls,cls) in a @classmethod
# see super_mult.py
result = D.m(D)
print("-----")
print(result)
