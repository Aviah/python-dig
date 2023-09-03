class Meal:
    _pasta: str = None

    @property
    # Decorator binds the 'pasta' symbol to a property object
    def pasta(self):
        return self._pasta

    print(f"pasta is now {pasta}")

    @pasta.setter
    # @pasta is the property object created above, setter is a decorator function, and a member of this object
    # Bind 'pasta' to a *new* property object (which uses the former for its methods)
    def pasta(self, pasta):
        self._pasta = pasta

    print(f"pasta is now {pasta}")

    @pasta.deleter
    # @pasta.deleter functionality is similar to @pasta.setter
    def pasta(self):
        self._pasta = None

    print(f"pasta is now {pasta}")


print(Meal.pasta)

m = Meal()
print(m.pasta)
m.pasta = 'pomodoro'
print(m.pasta)
del m.pasta
print(m.pasta)


print(Meal.pasta)
print(Meal.pasta.getter)
print(Meal.pasta.setter)
print(Meal.pasta.deleter)

print("getter")
print(Meal.pasta.getter(m).fget)
print(Meal.pasta.getter(m).fset)
print(Meal.pasta.getter(m).fdel)
print(m)

print("setter")
print(Meal.pasta.setter(m).fget)
print(Meal.pasta.setter(m).fset)
print(Meal.pasta.setter(m).fdel)

print("deleter")
print(Meal.pasta.deleter(m).fget)
print(Meal.pasta.deleter(m).fset)
print(Meal.pasta.deleter(m).fdel)
