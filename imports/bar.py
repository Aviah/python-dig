x = 200


def print_x(print_id=False):
    print(x)
    if print_id:
        print(id(x))


print(f"{__name__} imported")
