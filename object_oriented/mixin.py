# Mixins are placed on the left, and therefore precedent in the mro
# This is why they should not have __init__, and let Python find the __init__ on the main class
# to the left


class Account:
    _lang = 'English'

    def __init__(self, name, active=False):
        print("Account __init__invoked")
        self._name = name
        self._active = active
        # Uncomment and run: __init__ sets the instance's attr on __dict__, so lookup doesn't get to class/mixins
        # self._lang = 'Navajo'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def active(self):
        return self._active

    @property
    def language(self):
        return self._lang

    def greetings(self):
        return f"Greetings {self.name}"

    def goodbye(self):
        return f"Goodbye {self.name}"

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def status(self):
        return f"Account: {self.name} is {'active' if self.active else 'not active'}"


class ItalianMixin:
    _lang = 'Italian'

    def greetings(self):
        return f"Salve {self.name}"

    def goodbye(self):
        return f"Ciao {self.name}"


class PolishMixin:
    _lang = 'Polish'

    def greetings(self):
        return f"Pozdrowienia {self.name}"

    def goodbye(self):
        return f"Do widzenia {self.name}"


class ItalianAccount(ItalianMixin, Account):  # order is important
    pass


class PolishAccount(PolishMixin, Account):
    pass


bridget = Account(name='Bridget Jones', active=True)
leonardo = ItalianAccount(name='Leonardo Da-Vinchi')
wislawa = PolishAccount(name='Wisława Szymborska')

# most of the class functionality remains the same
print(bridget.status())
leonardo.activate()
print(leonardo.status())
wislawa.activate()
print(wislawa.status())

# mixin only for the customizations
print(bridget.greetings())
print(bridget.goodbye())
print(leonardo.greetings())
print(leonardo.goodbye())
print(wislawa.greetings())
print(wislawa.goodbye())

print(bridget.language)
print(vars(bridget))
print(leonardo.language)
print(wislawa.language)


# The order of the bases in the class declaration is important
# attr search will stop on the first find on the mro
print(bridget.__class__.__mro__)
print(type(leonardo).__mro__)
print(wislawa.__class__.__mro__)


class Partner:
    def __init__(self, name, company, title):
        self._name = name
        self._company = company
        self._title = title

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return f"Partner: {self.name}, {self.title} of {self.company}"


print("=====")


# Drop-in repeated functionality with mixing
# Caveat: the _lang attr is not used by the Partner class
class ItalianPartner(ItalianMixin, Partner):
    pass


class PolishPartner(Partner, PolishMixin):
    # order is not important here, only one base has the attribute
    pass


pasta = ItalianPartner('Giacomo Puccini', 'Pasta Inc.', 'CEO')
pierogi = PolishPartner('Fredrik Shopen', 'Pieorogi Inc.', 'CEO')
print(pasta)
print(pierogi)
print(pasta.greetings())
print(pierogi.goodbye())


print("=====")
# __init__ collisions


class FrenchMixin:
    def __init__(self):
        print("FrenchMixin __init__ invoked")
        self._greetings = 'Salutations'
        self._goodby = 'Au revoir'

    def greetings(self):
        return f"{self._greetings} {self.name}"

    def goodbye(self):
        return f"{self._goodby} {self.name}"


class FrenchAccount(FrenchMixin, Account):
    """__init__ collision: __init__ is an attribute
    the bases order affects where it's first found and run (once)
    see super_co.py
    """

    pass


try:
    victor = FrenchAccount(name='Victor Hugo')  # the mixin __init__ is not called
except TypeError as e:
    print(repr(e))


print("=====")
# __init__ collisions


class FrenchMixin:
    def __init__(self, *args, **kwargs):
        """now the __init__ signature with *args, **kwargs allows to instanciate
        will fail later when the attr is called"""
        print("FrenchMixin __init__ invoked")
        self._greetings = 'Salutations'
        self._goodby = 'Au revoir'

    def greetings(self):
        return f"{self._greetings} {self.name}"

    def goodbye(self):
        return f"{self._goodby} {self.name}"


class FrenchAccount(FrenchMixin, Account):
    pass


try:
    victor = FrenchAccount(name='Victor Hugo')
    print(victor.greetings())
except AttributeError as e:
    print(repr(e))

print("=====")
# works


class Common:
    _greetings = 'Hi'
    _goodbye = 'Bye'

    def greetings(self):
        return f"{self._greetings} {self.name}"

    def goodbye(self):
        return f"{self._goodby} {self.name}"


class FrenchMixin(Common):
    _greetings = 'Salutations'
    _goodby = 'Au revoir'


class FrenchAccount(FrenchMixin, Account):
    pass


victor = FrenchAccount(name='Victor Hugo')
print(victor.status())
print(victor.greetings())
print(victor.goodbye())
print(victor.language)  # _lang is missing on the mixin, picked the Account's attr (English)
