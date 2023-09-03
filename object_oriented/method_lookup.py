class AClass:
    def double_it(self, x):
        print(self)
        return x * 2


a = AClass()
print(a.double_it)
print(a.double_it(5))


a.double_it = lambda x: (x + 1000) * 2

print(a.double_it)
print(a.__dict__)
print(a.double_it(5))  # When found on the instance, don't pass the instance as self

delattr(a, 'double_it')
print(a.__dict__)
print(a.double_it(5))  # Back to attr search, call with instance as first argument
