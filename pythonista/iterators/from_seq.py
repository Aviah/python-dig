from itertools import chain

i = iter(range(5))
print(next(i))
print(next(i))


mylist = ['foo', 'bar', 'baz']
i = iter(mylist)
print(i)
print(next(i))
print(next(i))

mytuple = (100, 200, "300")
i = iter(chain(mylist, mytuple))
print(next(i))
print(next(i))
print(next(i))


print([x for x in mylist])
print([x for x in iter(mylist)])


chars = iter('abcdef')
print(next(chars))
print(list(chars))
