def get_decorator(custom_greetings):
    print(f"Enter get_decorator: {custom_greetings}")
    def outer(func):  # The actual decorator
        print(f"Enter outer: {func}")
        def inner():
            print("Enter inner")
            print(custom_greetings)
            func()
        return inner
    return outer


@get_decorator("Aloha!")  # Python evaluates this and send the result the func to decorate
def hi_there():
    print("Hi there!")


@get_decorator("Ciao!")
def hello():
    print("Hello!")

print(f"hi_there decorated by {hi_there}")
print(f"hello decorated by {hello}")

print("=====")
hi_there()
hello()
