class Metaclass(type):
    def __getattribute__(cls, item):
        print(f"Metaclass __getattribute__ invoked: {cls}.{item} ")
        return type.__getattribute__(cls, item)


class AClass(metaclass=Metaclass):
    def __getattribute__(self, item):
        print(f"AClass __getattribute__ invoked: {self}.{item}")
        return object.__getattribute__(self, item)

    def __len__(self):
        return 42

    def say_hi(self):
        return 'hi'


print(len(AClass()))  # implicit access to class special method: getattribute skipped
print(AClass.__len__)
print(AClass.say_hi)
a = AClass()
a.say_hi()
print(a.__len__)  # AClass.__getattribute__ invoked
print(len(a))     # AClass.__getattribute__ skipped, Python does direct lookup on type(a).__mro__