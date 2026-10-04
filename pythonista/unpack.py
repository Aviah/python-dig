print("===== Unpack to vars =====")
a, b, c = (100, 200, 300)
print(a)
a, b, c = [300, 400, 500]
print(b)
print("-----")
a, (b, c) = (10, (20, 30))
print(a)
print(b)
print(c)
print("-----")
a, b, *rest = range(10)
print(a)
print(b)
print(rest)
print("-----")
a, *rest, b = range(10)
print(a)
print(b)
print(rest)


print("\n===== Caller unpacking =====")

def f(pos1, pos2, pos3, kw1, kw2, kw3):
    print(pos1, pos2, pos3, kw1, kw2, kw3)


args = ('foo', 'bar', 'baz')
kwargs = dict(kw1='spam', kw2='eggs')
f(*args, kw1='spam', kw2='eggs', kw3='pool')
f(*args, **kwargs, kw3='jump')


def f2(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)

args = ('foo', 'bar', 'baz')
kwargs = dict(kw1='spam', kw2='eggs', bloop='whatever', pool='no')
f2(args, kwargs)  # w/o unpacking, both considered args
print("-----")
f2(*args, **kwargs)  # unpacking
print("-----")
f2()


print("\n===== Keyword only =====")

def f1_a(pos1, pos2, pos3, *, kw1, kw2, kw3):  # * enforces keyword-only args afterward (**kwargs not required)
    print(pos1, pos2, pos3, kw1, kw2, kw3)


f1_a('foo', 'bar', 'baz', kw1='spam', kw2='eggs', kw3='pool')
try:
    f1_a('foo', 'bar', 'baz', 'spam', 'eggs', 'pool')
except TypeError as e:
    print(repr(e))


def f1_b(*args, kw1, kw2, **kwargs):  # also enforces keyword-only args
    print(args, kw1, kw2, kwargs)


f1_b('foo', 'bar', kw1='baz', kw2='spam', **{'eggs': 'pool'})
f1_b('foo', 'bar', 'baz', kw1='spam', kw2='eggs', kw3='pool')
try:
    f1_b('foo', 'bar', 'baz', 'spam', **{'eggs': 'pool'})
except TypeError as e:
    print(repr(e))



print("\n===== Mixed =====")

args = ('foo', 'bar', 'baz')
kwargs = dict(kw1='spam', kw2='eggs')
def f3(pos1, *args, kw1, **kwargs):
    print(pos1)
    print(args)
    print(kw1)
    print(kwargs)

f3('jump', *args, 1000, **kwargs )
try:
    f3(args, kwargs)
except TypeError as e:
    print(repr(e))
f3(args, **kwargs)
print("-----")
f3(*args, **kwargs)

print("-----")
def with_kw(*, kw1, kw2):
    print(kw1, kw2)

with_kw(kw1='FOO', kw2='BAR')
with_kw(**{'kw1': 'FOO', 'kw2': 'BAR'})
with_kw(kw1='FOO', **{'kw2': 'BAR'})


print("\n===== Defaults =====")

def f4(pos1, pos2=None, pos3=None):
    print(pos1)
    print(pos2)
    print(pos3)

f4(args)
print("-----")
f4(*args)


print("\n===== Function does not unpack =====")

def f5(args, kwargs):  # w/o unpacking
    print(args)
    print(kwargs)

f5(args='pool', kwargs='bloop')
f5(args=(1, 2, 3), kwargs={'spam': 'eggs'})
try:
    f5(*(1, 2, 3), **{'spam': 'eggs'})
except TypeError as e:
    print(repr(e))

try:
    f5(*(1, 2, 3), kwargs={'spam': 'eggs'})
except TypeError as e:
    print(repr(e))

f5(*(1, 2))


print("\n===== Positional only =====")

def f6(country, city, /, **kwargs):  # positional-only args
    print(country)
    print(city)
    print(kwargs)


f6('Italy', 'Bologna')
try:
    f6('Italy', city='Bologna')
except TypeError as e:
    print(repr(e))

print("-----")

# Positional only is useful when the function arguments names collide with **kwargs
def f7(country, city, **kwargs):
    print(country)
    print(city)
    print(kwargs)


account_details = {'name': 'Guglielmo Marconi', 'city': 'Sasso-Marconi'}
try:
    f7('Italy', 'Sasso-Marconi', **account_details)  # fails
except TypeError as e:
    print(repr(e))


print("-----")

def f8(country, city, /, **kwargs):
    print(country)
    print(city)
    print(kwargs)


f8('Italy', 'Sasso-Markoni', **account_details)  # works
