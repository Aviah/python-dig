class DataDescriptor:
    """
    We have both __set__ and __delete__
    one of them is enough to be used as a data descriptor
    """

    def __set_name__(self, owner, name):
        print(f"Data Descriptor {self} __set_name__ called")
        self.owner_propery_name = name
        self.descriptor_attr_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        if obj is None:
            print("Called from class")
            return self
        print(f"Data Descriptor __get__ called {obj} {objtype}")
        return getattr(obj, self.descriptor_attr_name, None)

    def __set__(self, obj, val):
        print("Data Descriptor __set__ called")
        setattr(obj, self.descriptor_attr_name, val)

    def __delete__(self, obj):
        print("Descriptor __del__ called")
        delattr(obj, self.descriptor_attr_name)


class C:
    p1 = DataDescriptor()
    p2 = DataDescriptor()


class D:
    p3 = DataDescriptor()


c1 = C()
c2 = C()
print("=====")
c1.p1 = 42
print(c1.p1)
c1.p2 = 84
print(c1.p2)
del c1.p1
print(c1.p1)
print("=====")
print(C.p1)
print(C.p2)
print(D.p3)
print(vars(C)['p1'])
print(vars(C)['p2'])
print(vars(D)['p3'])
