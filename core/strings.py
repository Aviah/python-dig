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


print("\n===== Format =====")
print("{} {} {}".format(10, 20, 30))
print("{c} {b} {a}".format(a=10, b=20, c=30))
print("{1} {0} {2}".format('second', 'first', 'third'))
print('{:10}baz'.format('foo'))  # padding
print('{:^10}baz'.format('foo'))  # center in padding

baz = 100
print(f"{baz}")
print(f"{baz:.2f}")
print(f"{baz:08.2f}")
print("{:%Y-%b-%d %A}".format(datetime.datetime.now()))


print("\n===== Unicode =====")
s = "\u2602:\u2615:\u2708:\u270C"
print(s)
print(len(s))
print(type(s))  # string is in Unicode (1 or 2 or 4 bytes per char, by the max bytes required for any char in the str)
print([f"{x} is unicode {hex(ord(x))}" for x in s if x != ":"])
e = s.encode('UTF-8')
print(e)
print(type(e))
print(e.decode('UTF-8'))
print(type(e.decode('UTF-8')))

print(locale.getpreferredencoding())  # what Python currently used, may be custom from the system default
print(locale.getdefaultlocale())  # returns the locale, encoding
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
print(type(m))
print(m)
assert m == s
print(s.encode('unicode_escape'))  # https://docs.python.org/3/library/codecs.html#text-encodings
print(m.encode('unicode_escape'))
