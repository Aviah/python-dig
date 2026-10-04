from typing import NamedTuple

lst = [100, 'fooo', '100', 3, 'bar', 10, 80, 'spam']
try:
    print(sorted(lst))
except Exception as e:
    print(repr(e))
print(sorted(lst, key=lambda x: len(x) if isinstance(x, str) else x))
print(lst)
lst.sort(key=lambda x: len(x) if isinstance(x, str) else x)  # inplace
print(lst)

print("\n=====")
class Account(NamedTuple):
    id: str
    balance: float


a1 = Account('Smith', 100)
a2 = Account('Pronto', 10)
a3 = Account('Maybe', 1000)
a4 = Account('Sometimes', 100)

accounts1 = [a1, a2, a3, a4]
print(sorted(accounts1, key=lambda x: x.balance))
print(sorted(accounts1, key=lambda x: x.balance, reverse=True))
accounts2 = [a4, a2, a3, a1]
print(sorted(accounts2, key=lambda x: x.balance))
print(sorted(accounts2, key=lambda x: x.balance, reverse=True))

# stable
assert  sorted(accounts1, key=lambda x: x.balance) != sorted(accounts2, key=lambda x: x.balance)

# multiple keys
accounts3 = [a1, a2, a3, a4]
print(sorted(accounts3, key=lambda x: (x.balance, x.id)))
print(sorted(accounts3, key=lambda x: (x.id, x.balance)))
