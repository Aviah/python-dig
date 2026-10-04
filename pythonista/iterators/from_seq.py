from itertools import chain

i = iter(range(5))
print(next(i))
print(next(i))

print("-----")
mylist = ['foo', 'bar', 'baz']
i = iter(mylist)
print(i)
print(next(i))
print(next(i))


print("-----")
mytuple = (100, 200, "300")
i = iter(chain(mylist, mytuple))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


print("-----")
print([x for x in mylist])
print([x for x in iter(mylist)])


print("-----")
chars = iter('abcdef')
print(next(chars))
print(next(chars))
print(list(chars))
