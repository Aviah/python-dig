a, b, c = (100, 200, 300)
print(a)
a, b, c = [300, 400, 500]
print(b)
a, b, *rest = range(10)
print(a)
print(b)
print(rest)


print("=====")


def f(pos1, pos2, pos3, kw1, kw2, kw3):
    print(pos1, pos2, pos3, kw1, kw2, kw3)


args = ('foo', 'bar', 'baz')
kwargs = dict(kw1='spam', kw2='eggs')
f(*args, kw1='spam', kw2='eggs', kw3='pool')
f(*args, **kwargs, kw3='pool')
f('foo', 'bar', 'baz', 'spam', 'eggs', 'pool')


print("=====")


def f1a(pos1, pos2, pos3, *, kw1, kw2, kw3):
    print(pos1, pos2, pos3, kw1, kw2, kw3)


try:
    f1a('foo', 'bar', 'baz', 'spam', 'eggs', 'pool')
except TypeError as e:
    print(repr(e))  # single asterix enforces keyword arg


def f1b(*args, kw1, kw2, **kwargs):
    print(args, kw1, kw2, kwargs)


try:
    f1b('foo', 'bar', 'baz', 'spam', **{'eggs': 'pool'})
except TypeError as e:
    print(repr(e))  # another way to require keyword arguments

f1b('foo', 'bar', kw1='baz', kw2='spam', **{'eggs': 'pool'})

print("=====")


def f2(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)


f2(args, kwargs)  # w/o unpacking, both considered args
print("=====")
f2(*args, **kwargs)  # unpacking
print("=====")
f2()

print("=====")


def f3(pos1, *args, kw1, **kwargs):
    print(pos1)
    print(args)
    print(kw1)
    print(kwargs)


try:
    f3(args, kwargs)
except TypeError as e:
    print(repr(e))
f3(args, **kwargs)
print("=====")
f3(*args, **kwargs)

print("=====")


def f4(pos1, pos2=None, pos3=None):
    print(pos1)
    print(pos2)
    print(pos3)


f4(args)
print("=====")
f4(*args)


print("=====")


def f5(args, kwargs):  # w/o unpacking
    print(args)
    print(kwargs)


try:
    f5(*(1, 2, 3), **{'spam': 'eggs'})
except TypeError as e:
    print(repr(e))

try:
    f5(*(1, 2, 3), kwargs={'spam': 'eggs'})
except TypeError as e:
    print(repr(e))

f5(*(1, 2))
f5(args=(1, 2, 3), kwargs={'spam': 'eggs'})


print("=====")


def f6(country, city, /, **kwargs):  # positional only args
    print(country)
    print(city)
    print(kwargs)


f6('Italy', 'Bolongna')
try:
    f6('Italy', city='Bologna')
except TypeError as e:
    print(repr(e))

print("=====")
account_details = {'name': 'Guglielmo Marconi', 'city': 'Sasso-Marconi'}


def f7(country, city, **kwargs):
    print(country)
    print(city)
    print(kwargs)


try:
    f7('Italy', 'Sasso-Marconi', **account_details)  # fails
except TypeError as e:
    print(repr(e))


print("=====")


def f8(country, city, /, **kwargs):
    print(country)
    print(city)
    print(kwargs)


f8('Italy', 'Sasso-Markoni', **account_details)  # works
