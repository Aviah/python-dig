class DataDescriptor:
    """
    Simple data descriptor:
    From the outside it manages an attr like ordinary attr,
    yet it can do additional work when the attr is accessed and the descriptor is invoked

    Note:
    Here we have both __set__ and __delete__
    One of them is enough to be used as a data descriptor
    To get the priority of data descriptor for a __get__ only descriptor do something like

    def __set__(self, obj, val):
        raise NotImplementedError  # see descriptor_protocol.py
    """

    def __set_name__(self, owner, name):
        print(f"{self} __set_name__ invoked")
        self.owner_property_name = name
        self._internal_name = f'_{name}'

    def __get__(self, obj, objtype=None):
        if obj is None:
            print("Invoked from class")
            return self

        print(f"{self} __get__ invoked: {obj} {objtype}")
        return getattr(obj, self._internal_name, None)

    def __set__(self, obj, val):
        print(f"{self} __set__ invoked")
        setattr(obj, self._internal_name, val)


    def __delete__(self, obj):
        print(f"{self} __delete__ invoked")
        delattr(obj, self._internal_name)


class C:
    p1 = DataDescriptor()
    p2 = DataDescriptor()


class D:
    p3 = DataDescriptor()


c1 = C()
c2 = C()

print("\n=====")

c1.p1 = 42
print(c1.p1)
c1.p2 = 84
print(c1.p2)
c1.__dict__['p1'] = 999
print(c1.p1)  # still 42, data descriptor has precedence and wins
assert hasattr(c1, 'p1')

print("\n=====")

del c1.p1
print(c1.__dict__['p1'])
assert hasattr(c1, 'p1')
print(c1.p1)  # None, data descriptor wins: the *descriptor's* __get__ looks for _p1

print("\n=====")
print(C.p1)
print(C.p2)
print(D.p3)
print(vars(C)['p1'])
print(vars(C)['p2'])
print(vars(D)['p3'])
