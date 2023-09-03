from typing import NamedTuple


class Account(NamedTuple):
    id: str
    balance: float


a1 = Account('Smith', 100)
a2 = Account('Pronto', 10)
a3 = Account('Maybe', 1000)
a4 = Account('Sometimes', 100)

accounts = [a1, a2, a3, a4]
print(sorted(accounts, key=lambda x: x.balance))
print(sorted(accounts, key=lambda x: x.balance, reverse=True))
accounts = [a4, a2, a3, a1]
print(sorted(accounts, key=lambda x: x.balance))
print(sorted(accounts, key=lambda x: x.balance, reverse=True))  # stable
