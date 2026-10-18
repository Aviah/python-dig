"""
Abstract classes define and enforce an inheritance-based interface:
* They can require subclasses to implement selected methods and properties.
* They fit classic object-oriented hierarchies based on an "is-a" relationship.
* They can also provide shared implementation that subclasses inherit, override, or extend.
* Prefer them when the subclasses genuinely belong to the same conceptual hierarchy.

When you only need consumers to depend on some capability, without requiring a shared
inheritance hierarchy, a Protocol is often a better fit (see protocols.py).
"""


import abc
import hashlib
from typing import Self


class AbstractUser(abc.ABC):
    """
    Require subclasses to implement an interface:
    instance methods, properties, class methods, and static methods.
    """

    @abc.abstractmethod
    def verify_password(self, hashed_password:str) -> bool:
        ...

    @property
    @abc.abstractmethod
    def username(self) -> str:
        ...

    @username.setter
    @abc.abstractmethod
    def username(self, value:str) -> None:
        ...

    @classmethod
    @abc.abstractmethod
    def create_user(cls, username: str, password: str) -> Self:
        ...

    @staticmethod
    @abc.abstractmethod
    def hash_password(password:str) -> str:
        ...

    # Abstract class can provide concrete members like any other class.
    def __str__(self) -> str:
        return f"<User {self.username}>"

    def greet(self) -> None:
        print(f"{self.username} says Hi!")

class DbUser(AbstractUser):
    """
    DbUser *is-an* AbstractUser
    """

    def __init__(self, username, password):
        print("Found user in DB")
        self._username = username


    def verify_password(self, hashed_password:str) -> bool:
        print("Verified password on DB")
        return True

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

    @classmethod
    def create_user(cls, username: str, password: str) -> Self:
        print("Created user on DB")
        return cls(username, password)

    @property
    def username(self) -> str:
        print("Returned username from DB")
        return self._username

    @username.setter
    def username(self, value:str) -> None:
        print("Saved username to DB")
        self._username = value

    @property
    def db_id(self) -> int:
        # Can extend the abstract class
        return 1234

class ExternalServiceUser(AbstractUser):
    """
    ExternalServiceUser *is-an* AbstractUser
    """

    def __init__(self, username, password):
        print("Found user in service")
        self._username = username


    def verify_password(self, hashed_password:str) -> bool:
        print("Verified password on service")
        return True

    @staticmethod
    def hash_password(password: str) -> str:
        return hashlib.sha512(password.encode('utf-8')).hexdigest()

    @classmethod
    def create_user(cls, username: str, password: str) -> Self:
        print("Created user on service")
        return cls(username, password)

    @property
    def username(self) -> str:
        print("Returned username from service")
        return self._username

    @username.setter
    def username(self, value:str) -> None:
        print("Saved username to service")
        self._username = value

    @property
    def service_id(self) -> str:
        # Can extend the abstract class
        return "spameggs"


print("\n")

dbu = DbUser('Homer', 'abc')
print(dbu.username)
print(dbu.hash_password('abc'))
print(dbu.verify_password('xyz'))
dbu.greet()
dbu.username = "Homer Simpson"
print(dbu.username)
print(dbu.db_id)
dbu1 = DbUser.create_user('Marge Simpson', 'foo')
print(dbu1)


print("\n")

esu = ExternalServiceUser('John', 'abc')
print(esu.username)
print(esu.hash_password('abc'))
print(esu.verify_password('xyz'))
esu.greet()
esu.username = 'John Doe'
print(esu.username)
print(esu.service_id)
esu1 = ExternalServiceUser.create_user('Paul', 'pennylane')
print(esu1)

print("\n===== Abstract classes enforce implementation =====")

try:
    AbstractUser()
except TypeError as e:
    print(repr(e))  # Can't instantiate the abstract class directly.


class BrokenUser(AbstractUser):
    ...

try:
    BrokenUser()
except TypeError as e:
    print(repr(e))  # BrokenUser hasn't implemented the required abstract members



