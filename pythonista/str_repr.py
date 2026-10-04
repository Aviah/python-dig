# __repr__ should give a more debug-oriented info

class User:

    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return f"<User: {self.name}>"

user = User("John Doe")
print(user)  # str
print(repr(user))

print("\n=====")

class AsIs:
    pass


class JustStr:
    def __str__(self):
        return "It's 42"


class JustRepr:
    def __repr__(self):
        return "Whatever"


class BothStrRepr:
    def __str__(self):
        return "It's 42"

    def __repr__(self):
        return "Whatever"


print(str(AsIs()))
print(repr(AsIs()))
print(str(JustStr()))
print(repr(JustStr()))

# __str__ falls back to __repr__
print(str(JustRepr()))

print(repr(JustRepr()))
print(str(BothStrRepr()))
print(repr(BothStrRepr()))
