# Similar effect to mixins, Account deliberately delegates through super(),
# allowing another implementation to be inserted into the mro, and change the original behaviour
# see mixins.py


class DefaultLang:
    _lang = 'English'

    def greetings(self):
        print(f"Hi {self.name}")

    def goodbye(self):
        print(f"Bye {self.name}")


class ItalianLang(DefaultLang):
    _lang = 'Italian'

    def greetings(self):
        print(f"Salve {self.name}")

    def goodbye(self):
        print(f"Ciao {self.name}")


class Account(DefaultLang):
    def __init__(self, name):
        self.name = name

    def somebody_enters(self):
        super().greetings()

    def somebody_leaves(self):
        super().goodbye()


a = Account('John')
print(a)
print(type(a).__mro__)
a.somebody_enters()
a.somebody_leaves()


print("\n=====")

class ItalianAccountWrong(ItalianLang, Account):  # Fails
    """ItalianLang precedes Account in the mro

    This ordering works for mixin with ordinary attr lookup
    But not for super() and the mro: The super() inside account continues in the mro *after* account
    So it will not get to ItalianLang, and reach DeafultLang
    """
    pass


i = ItalianAccountWrong('Federico')
print(type(i).__mro__)
i.somebody_enters()
i.somebody_leaves()


print("\n=====")

# Unlike the mixin pattern, it should appear to the *right*
# So it's to the *right* of Account, and picked by super() mro lookup
class ItalianAccount(Account, ItalianLang):  # Works
    """
    mro based delegation (kind of dependency injection)

    super() from Account gets to ItalianLang by mro
    ItalianLang is now *after* Account, but *before* DefaultLang
    Since it's a subclass of DefaultLang, therefore must appear before it in the mro
    """
    pass


i = ItalianAccount('Federico')
print(type(i).__mro__)
i.somebody_enters()  # subclass before the parent class, so ItalianLang before DefaultLang
i.somebody_leaves()