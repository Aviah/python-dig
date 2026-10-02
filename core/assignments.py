

a = 1
b = 2
c = 3
d = 4
print(a,b,c,d)

a = b = c = d = 100
print(a,b,c,d)

a,b,c,d = 1000, 2000,3000, 4000
print(a,b,c,d)

a,b = b, a
print(a,b,c,d)

a, b, *c = ['foo', 'baz', 'spam', 'bloop']
print(a, b, c)

a, *b, c = ['foo', 'baz', 'spam', 'bloop']
print(a, b, c)

try:
    a, b, c = 1, (2, 3)
except Exception as e:
    print(repr(e))

a, (b, c) =  1, (2, 3)
print(a, b, c)


a = [2, 4, 6, 8, 10]
b = [2, 4, 6, 8, 10]
print(a)
print(b)
assert a == b

b[0] = 200
print(a)
print(b)

a = b  # Binding. This is not an assignment, the symbol "a" now points to the same object that "b" points to
print(a)
print(b)
b[0] = 99999
print(a)
print(b)
assert  a is b


class A: pass
a = A()
a.prop = 123456
print(a.prop)

