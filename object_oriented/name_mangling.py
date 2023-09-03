# Name mangling is helpful for letting subclasses override methods without breaking intraclass method calls
# https://docs.python.org/3/tutorial/classes.html#private-variables
class User:
    def __init__(self, *args, **kwargs):
        self.__scope = "General"

    def __say(self):
        print("Hi User")


class Marge(User):
    def __init__(self, *args, **kwargs):
        self.__scope = "Marge"

    def __say(self):
        print("Hi Marge")


class Homer(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__scope = "Homer"

    def __say(self):
        print("Hi Homer")


u = User()
print(u._User__scope)
print(hasattr(u, '__scope'))

m = Marge()
print(m._Marge__scope)
print(hasattr(u, '__scope'))

h = Homer()
print(h._Homer__scope)
print(h._User__scope)
print(hasattr(h, '__scope'))

u._User__say()
m._Marge__say()
h._Homer__say()
h._User__say()
