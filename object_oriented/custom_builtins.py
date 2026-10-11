print("===== Custom list ====")

class PopulatedList(list):
    def __init__(self, list_len, default):
        self._default = default
        list.__init__(self)
        for i in range(list_len):
            self.append(default)

    def __getitem__(self, item):
        try:
            res = list.__getitem__(self, item)
            if isinstance(res, slice):
                new_pl = PopulatedList(0, self._default)
                new_pl.extend(res)
                return new_pl
            return res
        except IndexError as e:
            print(repr(e))


print(PopulatedList(5, 100))
print(PopulatedList(2, 10))
p = PopulatedList(10, 3)
print(p)
print(p[5])
x = p[1000]  # No index error
assert p[1000] is None
p[1], p[2] = 200, 201
print(p)
print(p[1:5])
print(type(p[1:5]))


print("\n===== Custom dict ====")

class CustomDict(dict):

    def __getitem__(self, item):

        if item == 'spam':
            return 'eggs'

        return super().__getitem__(item)


d = CustomDict()
d['foo'] = 'baz'
assert 'foo' in d
assert 'spam' not in d  # we didn't customise __contains__, so it does not match the customised __getitem__
print(d['spam'])