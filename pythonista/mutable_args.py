def f1(mylist):
    mylist.append('pineapple')  # The local name is bound to an object that is owned by the caller


def f2(mylist):
    mylist = mylist  # Does nothing: the local name is already bound to this list object (as an arg)
    mylist.append('watermelon')


def f3(mylist):
    mylist = mylist[:]  # binding to a NEW object
    mylist.append('grapes')


fruits = ['apple', 'cherry']
print(fruits)
f1(fruits)
print(fruits)
f2(fruits)
print(fruits)
f3(fruits)
print(fruits)
