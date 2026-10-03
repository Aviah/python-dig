# General purpose function that injects any function as a decorator


def make_decorator(decorator):
    def get_decorator(*args, **kwargs):  # Same as decorator_param.py
        def outer(func):  # It's common to call this function "outer"
            def inner(*func_args, **func_kwargs):
                decorator(*args, **kwargs)
                return func(*func_args, **func_kwargs)

            return inner

        return outer

    return get_decorator


@make_decorator  # Now the decorated function is a decorator (the get_decorator closure)
def custom_greetings(greetings: str, times: int):
    print(f"{greetings} " * times)

print(f"custom_greetings is {custom_greetings}")


@custom_greetings("Aloha!", 2)
def hi_there():
    print("Hi there!")

print(f"hi_there is {hi_there}")

@custom_greetings("Ciao!", 3)
def hello(is_upper=False):
    response = "Hello!"
    if is_upper:
        response = response.upper()
    print(response)

print(f"hello is {hello}")

print("=====")
hi_there()
hello(is_upper=True)
