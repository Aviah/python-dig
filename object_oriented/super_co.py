# Similar functionality to mixins, see mixin.py
# Maybe easier to provide default parent class, and work with changed order of components with the mro


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

print("=====")


class ItalianAccountWrong(ItalianLang, Account):  # Fails
    """Nothing happens
    ItalianLang to the left, therefore it precedes Account in the mro
    Thus super() from Account doesn't grab it, and still gets to DefaultLang"""

    pass


i = ItalianAccountWrong('Fedrico')
print(type(i).__mro__)
i.somebody_enters()
i.somebody_leaves()

print("=====")


class ItalianAccount(Account, ItalianLang):  # Works
    """Dependency injection:
    super() gets to ItalianLang by mro, since it's now *after* Account,
    but before DefaultLang (it's a subclass of DefaultLang, so before it)"""

    pass


i = ItalianAccount('Fedrico')
print(type(i).__mro__)
i.somebody_enters()  # subclass before the parent class, so ItalianLang before DefaultLang
i.somebody_leaves()
