# repr should give more detailed and debug-oriented info
class AsIs:
    pass


class JustStr:
    def __str__(self):
        return "42 what else"


class JustRepr:
    def __repr__(self):
        return "Whatever"


class BothStrRepr:
    def __str__(self):
        return "42 what else"

    def __repr__(self):
        return "Whatever"


print(str(AsIs))
print(repr(AsIs))
print(str(JustStr()))
print(repr(JustStr()))
print(str(JustRepr()))  # unmodified str used modified repr
print(repr(JustRepr()))
print(str(BothStrRepr()))
print(repr(BothStrRepr()))
