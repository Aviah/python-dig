"""
This is the same demo as abs_class.py, with one addition: a custom metaclass.

Subclassing abc.ABCMeta lets a custom metaclass add its own class-creation
behaviour while preserving abstract-method enforcement.
"""


import abc
import hashlib
from typing import Self


class Metaclass(abc.ABCMeta):

    def __new__(mcls, name, bases, attrs, **kwargs):

        print(f"Creating new class {name} | {bases} | {attrs} ")
        private = kwargs.pop('private', False)
        if private:
            print("This class must be private!")

        return super().__new__(mcls, name, bases, attrs)


class AbstractUser(metaclass=Metaclass, private=True):
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


dbu = DbUser('Homer', 'abc')
print(dbu.username)
dbu.greet()
print(dbu.db_id)

print("\n=====")
class BrokenUser(AbstractUser):
    ...

try:
    BrokenUser()
except TypeError as e:
    print(repr(e))  # BrokenUser hasn't implemented the required abstract members