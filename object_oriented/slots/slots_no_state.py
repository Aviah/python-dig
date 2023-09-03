class AClass:
    __slots__ = []
    x = 100

    def print_something(self):
        print('something')

    @classmethod
    def print_something_else(self):
        print('something else')


a = AClass()
a.print_something()
a.print_something_else()
print(a.x)
print(a.__slots__)
a.x = 200  # read only
