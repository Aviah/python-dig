def f6(mylist):
    mylist.append('pineapple')


def f7(mylist):
    mylist = mylist
    mylist.append('watermelon')


def f8(mylist):
    mylist = mylist[:]
    mylist.append('grapes')
    print(mylist)


fruits = ['apple', 'cherry']
print(fruits)
f6(fruits)
print(fruits)
f7(fruits)
print(fruits)
f8(fruits)
print(fruits)
