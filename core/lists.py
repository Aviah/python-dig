outer_loop = [1, 2, 3, 4]
nested_loop = ['foo', 'bar', 'baz']

print([*outer_loop, *nested_loop])
print([(x, y) for y in nested_loop for x in outer_loop])
print([x for x in nested_loop if x.startswith('f')])
print(
    [element for element in nested_loop if element.startswith('b') and element.endswith('r')]
)  # readability, PEP8 line length
l1 = [x for x in outer_loop if x > 2]
print(l1)
t = tuple([x for x in outer_loop if x <= 2])
print(t)
from itertools import chain

print([x for x in chain(outer_loop, ['spam', 'eggs'])])

print("=====")
l2 = outer_loop.extend(nested_loop)
print(l2)
print(outer_loop)


print(outer_loop.sort(key=lambda x: x if type(x) == int else len(x)))
print(outer_loop)

l2 = outer_loop + nested_loop
print(l2)
l2.remove('foo')
print(l2)
del l2[6]
print(l2)

""" Accept not existing right boundary slice, by design
https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
The slice of s from i to j is defined as the sequence of items with index k such that i <= k < j. 
If i or j is greater than len(s), use len(s)"""
print(len(outer_loop))
print(outer_loop[0:50])
