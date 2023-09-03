import locale


def print_the_file():
    with open('foo.txt', 'r') as f:
        print(f.read())

    print("=====")


with open('foo.txt', 'w') as f:
    f.write("Hi there!\n")

with open('foo.txt', 'w') as f:
    f.write("Hi there!\n")

with open('foo.txt', 'a') as f:
    f.write("Say cheese\n")

print_the_file()

with open('foo.txt', 'w') as f:
    f.write("Luggnagg\n")

print_the_file()
with open('foo.txt', 'a+') as f:
    f.write("Glubbdubdrib\n")
    print("-----")
    print(f.read())
    print("-----")
    f.seek(0)
    print(f.read())


with open('foo.txt', 'w+') as f:
    f.write("Houyhnhnms\n")
    f.write("Houyhnhnms\n")
    f.seek(0)
    print(f.read())

print_the_file()
with open('foo.txt', 'w') as f:
    f.write("Luggnagg\n")
    f.seek(0)
    f.write("Luggnagg\n")
    print_the_file()
    try:
        f.read()
    except Exception as e:
        print(repr(e))  # no +


with open('data.txt', 'r') as f:
    print(next(f))
    print(next(f))
    f.seek(0)
    print(next(f))

# unicode
with open('baz.txt', 'r') as f:
    print(f.read())  # default encoding by context $LANG

with open('baz.txt', 'rb') as f:
    print(f.read())

with open('baz.txt', 'r', encoding='UTF-8') as f:
    print(f.read())

with open('baz.txt', 'r', encoding='ANSI_X3.4-1968') as f:  # ASCII encoding
    print(f.read())  # fails, non ASCII
