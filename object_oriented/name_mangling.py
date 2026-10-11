"""
Name mangling is helpful for preventing subclass attr collision
without breaking intraclass method calls
"""

class User:
    def __init__(self, *args, **kwargs):
        self.__scope = "General"

    def __say(self):
        print("Hi User")

    def greet(self):
        self.__say()


class Marge(User):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
print(m._User__scope)
print(hasattr(m, '__scope'))

h = Homer()
print(h._Homer__scope)
print(h._User__scope)
print(hasattr(h, '__scope'))

m._Marge__say()
h._Homer__say()

# Does not override
u._User__say()
m._User__say()
h._User__say()

print("\n=====")
# Does not take the actual subclass __say method.
# Mangled when the class is built
m.greet()
h.greet()


try:
    m.__say()
except AttributeError as e:
    print(repr(e))  # name was mangled, can't call it directly