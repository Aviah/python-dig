import datetime
import locale

s = "abcde"
print(s[4])
try:
    s[4] = 'm'
except TypeError:
    print("Immutable")

[print(x) for x in s]
print(s[0:])
print(s[-1])
print(s[0:50])

print("{} {} {}".format(10, 20, 30))
print("{c} {b} {a}".format(a=10, b=20, c=30))
print("{1} {0} {2}".format('first', 'second', 'third'))
print('{:10}baz'.format('foo'))
print('{:^10}baz'.format('foo'))

baz = 100
print(f"{baz}")
print(f"{baz:.2f}")
print(f"{baz:08.2f}")
print("{:%Y-%b-%d %A}".format(datetime.datetime.now()))


print("=====")
s = "\u2602:\u2615:\u2708:\u270C"
print(s)
print(len(s))
print(type(s))  # string is unicode
e = s.encode('UTF-8')
print(e)
print(type(e))
print(e.decode('UTF-8'))
print(type(e.decode('UTF-8')))

print(locale.getpreferredencoding())
print(locale.getdefaultlocale())
print(type(b"Hello"))
print(type(b"Hello".decode('UTF-8')))
assert not "Hello" == b"Hello"
try:
    "Hello" + b"Hello"
except TypeError:
    print("Will not coerce")

assert b"Hello" not in {"Hello": "I'm a string"}

# https://www.unicode.org/Public/UCD/latest/ucd/NamesList.txt
m = "\N{UMBRELLA}:\N{HOT BEVERAGE}:\N{AIRPLANE}:\N{VICTORY HAND}"
print(m)
assert m == s
print(s.encode('unicode_escape'))  # https://docs.python.org/3/library/codecs.html#text-encodings
print(m.encode('unicode_escape'))
