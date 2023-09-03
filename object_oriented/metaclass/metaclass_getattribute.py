class Meta(type):
    def __getattribute__(cls, item):
        print("Meta __getattribute__ invoked")
        return type.__getattribute__(cls, item)


class AClass(metaclass=Meta):
    def __getattribute__(self, item):
        print("AClass __getattribute__ invoked")
        return object.__getattribute__(self, item)

    def __len__(self):
        return 42

    def say_hi(self):
        return 'hi'


print(len(AClass()))  # implict access to class special method: getattribute skipped
print("=====")
print(AClass.__len__)
print(AClass.say_hi)
print(AClass.__len__())  # fails, should be used by the instance with self
