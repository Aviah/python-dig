# + makes the mode readable and writable; it does not affect file creation
# r: read, file must exist
# w: write, create if needed, otherwise truncate; start at beginning
# a: append, create if needed, writes always go to the end

def print_the_file():
    with open('foo.txt', 'r') as f:
        print(f.read())

    print("\n=====")


with open('foo.txt', 'w') as f:
    f.write("Hi there!\n")

with open('foo.txt', 'w') as f:
    f.write("Hi there again!\n")

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


with open('foo.txt', 'a+') as f:
    f.write('Laputa\n')
    f.seek(0)
    f.write('Utopia')  # with a write always goes to the end

print_the_file()



# Unicode
print("\n===== Unicode =====")

with open('baz.txt', 'r') as f:
    print(f.read())  # default encoding by context $LANG, from 3.15 it's UTF-8

with open('baz.txt', 'rb') as f:
    print(f.read())

with open('baz.txt', 'r', encoding='UTF-8') as f:
    print(f.read())

try:
    with open('baz.txt', 'r', encoding='ANSI_X3.4-1968') as f:  # ASCII encoding
        print(f.read())  # fails, non ASCII
except Exception as e:
    print(repr(e))

s = "\u2602:\u2615:\u2708:\u270C"
with open('/tmp/blah.txt', 'w') as f:
    f.write(s)  # default encoding on write is UTF-8

with open('/tmp/blah.txt', 'r') as f:
    print(f.read())  # default encoding on read is UTF-8

try:
    with open('/tmp/blah.txt', 'r', encoding='ascii') as f:
        print(f.read())  # default encoding is UTF-8
except UnicodeDecodeError as e:
    print(repr(e))

# restores foo.txt
with open('foo.txt', 'w') as f:
    f.write('Luggnagg')
