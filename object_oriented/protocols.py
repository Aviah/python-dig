"""
Protocols describe an interface structurally:
* A class can implement the protocol *without inheriting* from it.
* A protocol typically describes one capability or aspect of a class's interface,
not necessarily the class's entire functionality.
* E.g. the Iterable protocol: users, payments, or files may belong to completely
different class hierarchies, but all can implement the same iteration capability.
* The protocol itself should be simple and focused,
and should not be aware of or handle complexity unrelated to the capability it describes.
* Protocols promote decoupling: consumers depend on a small required interface,
not on the concrete class or its unrelated functionality.

For interface of well defined class hierarchies, see abs_class.py

Note:
@runtime_checkable is only needed for isinstance()/issubclass() checks.
Static type checkers do not require it and can report incompatible implementations.
"""

import typing
import uuid


@typing.runtime_checkable
class User(typing.Protocol):

    def token(self) -> str:
        ...


@typing.runtime_checkable
class Greetings(typing.Protocol):

    def say_hi(self) -> None:
        ...

    def say_bye(self) -> None:
        ...



class ItalianUser:
    """
    No Greetings inheritance
    No User inheritance
    """
    _name: typing.Optional[str] = None

    def token(self) -> str:
        return str(uuid.uuid4())

    def say_hi(self) -> None:
        print("Salve!")

    def say_bye(self) -> None:
        print("Ciao!")

    @property
    def name(self) -> typing.Optional[str]:
        return self._name

    @name.setter
    def name(self, value: typing.Optional[str]) -> None:
        self._name = value


assert  issubclass(ItalianUser, Greetings)
assert isinstance(ItalianUser(), Greetings)
assert issubclass(ItalianUser, User)
assert isinstance(ItalianUser(), User)

iu = ItalianUser()
iu.name = 'Federico'
print(iu.name)
iu.say_hi()
iu.say_bye()


print("\n=====")

def greet(greeter: Greetings) -> None:
    # The function requires the Greetings *interface*, not inheritance from Greetings.
    # Protocol says: "anything with this interface implementation is acceptable here”
    greeter.say_hi()
    greeter.say_bye()

greet(ItalianUser())