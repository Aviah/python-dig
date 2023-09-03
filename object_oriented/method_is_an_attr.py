class Calc:
    def double_it(self, x):
        return x * 2

    def tripple_it(self, x):
        return x * 3


c = Calc()
d = getattr(c, 'double_it')
t = getattr(c, 'tripple_it')

print(d(10))
print(t(10))
