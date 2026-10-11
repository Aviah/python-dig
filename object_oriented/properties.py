from typing import Optional


class Meal:
    _pasta: Optional[str] = None

    @property
    # Decorator binds the 'pasta' symbol in the class namespace to a property object
    def pasta(self):
        print(f"Property pasta getter invoked")
        return self._pasta

    print(f"pasta is now {pasta}")  # 1st property object

    """
    pasta is now the property object created above (1st), with the getter decorator
    The pasta.setter is a decorator function, and a member of the 1st property object
    Every property object is also a factory of new property object
    @pasta.setter is a decoration expression that creates new property object
    Here, the 1st property object returns a 2nd property object
    For the 2nd: setter is the decorated setter function, while the getter and deleter are copied from the 1st
    """
    @pasta.setter
    def pasta(self, pasta):
        print(f"Property pasta setter invoked on {type(self)}")
        self._pasta = pasta

    print(f"pasta is now {pasta}")  # new property object, does not mutate the existing one

    """Same idea:
    @pasta.deleter returns new property object, the 3rd
    The 3rd getter and setter are copied from the 2nd, and the deleter is the decorated deleter function
    """
    @pasta.deleter
    def pasta(self):
        print(f"Property pasta deleter invoked")
        self._pasta = None

    print(f"pasta is now {pasta}")


print(Meal.pasta)

m = Meal()
print(m.pasta)
m.pasta = 'pomodoro'
print(m.pasta)
del m.pasta
print(m.pasta)  # None, was set by the deleter

print("\n===== Property factory: new objects and inheritance")
# Allows subclass to override getter or setter or deleter w/o mutating the parent

class AnotherMeal(Meal):

    @Meal.pasta.deleter
    def pasta(self):
        self._pasta = "Gnocchi"


m1 = Meal()
m2 = AnotherMeal()
assert Meal.pasta is not AnotherMeal.pasta  # Subclass created new property, that uses the original getter and setter
assert Meal.pasta.fget is AnotherMeal.pasta.fget
assert Meal.pasta.fset is AnotherMeal.pasta.fset
assert Meal.pasta.fdel is not AnotherMeal.pasta.fdel  # replaced by the subclass
m1.pasta = "Arrabiata"
m2.pasta = "Fetuccini Alfredo"
print(m1.pasta)
print(m2.pasta)
del m1.pasta
del m2.pasta
print(m1.pasta)
print(m2.pasta)



print("\n===== Property object =====")

print(Meal.pasta)
Meal.pasta = Meal.pasta.getter(lambda x: "Pesto")
print(m.pasta)
print(AnotherMeal().pasta)  # AnotherMeal property is still the original getter
Meal.pasta = Meal.pasta.deleter(lambda x: setattr(x, '_pasta', "Mushrooms"))
print(m.pasta)
del m.pasta
print(m.pasta)  # still the Pesto getter
Meal.pasta = Meal.pasta.getter(lambda x: x._pasta)
print(m.pasta)
print(Meal.pasta.fget)  # The plain getter function
print(Meal.pasta.fset)  # The plain setter function
print(Meal.pasta.fdel)  # The plain deleter function

class Foo:
    _pasta = "Preferring pizza!"

print(Meal.pasta.fget(Foo()))


