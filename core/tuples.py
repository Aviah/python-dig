t = (200, 100, 300, 400, 600)
print(t[1])
try:
    t[1] = 1000
except Exception as e:
    print(repr(e))  # immutable

print(sorted(t))  # to list, then sort

m = ()
print(type(m))
m = (10,)
print(type(m))
m = 10,  # non idiomatic, common mistake to forget a comma at the end of the line
print(type(m))

a, b, c, d, e = t
print(a)
print(b)
a, b, *the_rest = t
print(a)
print(b)
print(the_rest)


t = (100, 'a', 'b', 200)  # sorted as is will fail
print(sorted(t, key=lambda x: len(x) if type(x) is str else x))


print("\n===== Named Tuple =====")
from typing import NamedTuple

class Account(NamedTuple):
    id: int
    name: str
    balance: float


a = Account(123456, 'John Doe', 1000)
print(a)
assert isinstance(a, tuple)
print(type(a))
print(a.name)
assert hasattr(a, '__iter__')  # unlike dataclass
print([x for x in a])

try:
    a.name = 'Another name'
except Exception as e:
    print(repr(e))  # fails, unlike default dataclass
