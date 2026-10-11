print("===== A method is an attribute =====")
class Calc:
    def double_it(self, x):
        return x * 2

    def triple_it(self, x):
        return x * 3


c = Calc()
d = getattr(c, 'double_it')
t = getattr(c, 'triple_it')
print(d)
print(t)
print(d(10))
print(t(10))



print("===== Method shadowing by instance =====")
# The actual method lookup is more complex, see the descriptor demos
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

# When found on the instance, don't pass the instance as self: plain function, no binding, no __get__ call
# Finding it on the __dict__ does not trigger lookup, and thus does not trigger a descriptor and binding
print(a.double_it(5))

delattr(a, 'double_it')
print(a.__dict__)
print(a.double_it(5))  # Back to attr search, call with instance as first argument

