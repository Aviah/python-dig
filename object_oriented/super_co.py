# similar functionality to mixins, see mixin.py
# maybe easier to provide default parent class, and work with changed order of components with the mro


class DefaultLang:
    _lang = 'English'

    def greetings(self):
        print(f"Hi {self.name}")

    def goodbye(self):
        print(f"Bye {self.name}")


class ItalianLang:
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


class ItalianAccount(Account, ItalianLang):
    pass


print("=====")
i = ItalianAccount('Fedrico')
print(type(i).__mro__)
i.somebody_enters()
i.somebody_leaves()
