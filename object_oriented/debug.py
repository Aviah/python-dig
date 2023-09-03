class AClass:
    def __call__(self):
        print("42")


a = AClass()
a()


def print_something():
    print("something")


a.__call__ = print_something
a()
print(a.__call__)
