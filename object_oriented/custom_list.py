class PopulatedList(list):
    def __init__(self, list_len, default):
        list.__init__(self)
        for i in range(list_len):
            self.append(default)

    def __getitem__(self, item):
        try:
            return list.__getitem__(self, item)
        except IndexError as e:
            print(repr(e))


print(PopulatedList(5, 100))
print(PopulatedList(2, 10))
p = PopulatedList(10, 3)
print(p)
print(p[5])
x = p[1000]
print(p[1:5])
