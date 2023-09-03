s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4, 5}
s3 = {1, 2, 3, 100, 200}
s4 = {2, 3, 1000}

assert s2 >= s1
assert not s3 > s1
print(s3 - s1)
print(s3 ^ s1)
assert (s3 - s1) != (s1 - s3)
assert (s3 ^ s1) == (s1 ^ s3)
assert {'a', 'b', 'c'}.isdisjoint(s1)
print(s3 - s2)
print(s1 | s2 | s3 | s4)
print(s1 & s2 & s3 & s4)


# set comprehension
print({x for x in range(0, 20, 2)})
