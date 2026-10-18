import datetime
from functools import partial
import sys
import weakref


class AClass:
    foo = 'baz'

    def say_hi(self, label):
        print(f"Hello from {label}!")

a = AClass()

print("\n##### Strong and weak refs, reference count")
print(f"a ref count: {sys.getrefcount(a)}")  # always +1, since the call to getrefcount is another strong ref
aa = a
print(f"a ref count: {sys.getrefcount(a)}")
aaa = a
print(f"a ref count: {sys.getrefcount(a)}")
a.say_hi('a')

print("\n----- weakref ref")
# Access the weak reference itself
awref1 = weakref.ref(a)
print(awref1())
print(f"a ref count: {sys.getrefcount(a)}")
print(f"a weakref count: {weakref.getweakrefcount(a)}")
awref1()
assert awref1() is a  # dereference and provide the object itself
awref1().say_hi('awref1')

print("\n----- weakref proxy")
# Python forwards operations to the object. No explicit dereference is needed,
# but you have less access to the weak-reference object itself.

awrefp2 = weakref.proxy(a)
print(awrefp2)  # no need to de-reference
print(f"a ref count: {sys.getrefcount(a)}")
print(f"a weakref count: {weakref.getweakrefcount(a)}")
awrefp2.say_hi('awref2')
assert awrefp2 == a
assert awrefp2 is not a  # proxy

del a
try:
    print(f"a ref count: {sys.getrefcount(a)}")
except NameError as e:
    print(repr(e))
del aa, aaa
assert awref1() is None
try:
    print(awrefp2)
except ReferenceError as e:
    print(repr(e))


print("\n===== Callback =====")

refs = {}
def notify(wkref, message, registry):
    print(message)
    if isinstance(wkref, weakref.ProxyTypes):
        # The referred to object is dead, but the proxy object itself is still available to the callback.
        # Forwarded operations fail, but id() and type checks work.
        # So it can be removed from mappings
        del registry[id(wkref)]
    else:
        # You get the ref object itself (unlike the forward of the proxy)
        del registry[wkref]


callback = partial(notify, message='Callback invoked: AClass object deleted', registry=refs)


a = AClass()
awref = weakref.ref(a, callback)
refs[awref] = datetime.datetime.now().isoformat()
print(awref.__callback__)
assert awref.__callback__ is callback

awrefp = weakref.proxy(a, callback)
refs[id(awrefp)] = datetime.datetime.now().isoformat()  # proxy is *not* hashable
# Can't retrieve the callback with oficial API, proxy forwards to the object
print(refs)
del a
print(refs)


print("\n===== Cached weakrefs =====")

class SomeClass:
    ...


def callback1(wkrf):
    print('foo')


def callback2(wkrf):
    print('bar')

s = SomeClass()
wr1 = weakref.ref(s)
wr2 = weakref.ref(s)
print(wr1, wr2)
assert wr1 is wr2  # CPython reuses the callback-less weakref for the same object

wr3 = weakref.ref(s, callback1)
wr4 = weakref.ref(s, callback2)
print(wr3, wr4)
assert wr3 is not wr4

assert wr1() is wr3()


print("\n===== Weakref builtins =====")

d = {'foo': 'baz'}
try:
    dwref = weakref.ref(d)
except TypeError as e:
    print(repr(e))  # Not all built-in types support weak reference

s = set([1, 2, 3])
swref = weakref.ref(s)
print(swref())  # weakrefable

class MyDict(dict):
    ...

d = MyDict(foo='baz')
dwref = weakref.ref(d)
print(dwref())  # works


print("\n===== Descriptor example =====")

class LogDescriptor:
    """For demo, assume one usage of this descriptor per class"""
    def __init__(self, use_weakrefs=False):
        if use_weakrefs:
            self._storage = weakref.WeakKeyDictionary({})
            self._log = weakref.WeakKeyDictionary({})
        else:
            # Memory leak
            self._storage = {}
            self._log = {}

    def __get__(self, instance, owner):
        if instance is None:
            return  self

        return self._storage.get(instance)

    def __set__(self, instance, value):
        self._storage[instance] = value
        self._log[instance] = datetime.datetime.now().isoformat()


    def show_log(self):
        print(self._log)

class UserMemLeak:
    name = None
    token = LogDescriptor()

    def __repr__(self) -> str:
        return (f"<User object: {self.name}>")

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} deleted")

alice = UserMemLeak(name='Alice')
bob = UserMemLeak(name='Bob')
alice.token = 123
bob.token = 456
print(alice.token)
print(bob.token)
UserMemLeak.token.show_log()
del alice
del bob
try:
    print(alice)
except NameError as e:
    print(repr(e))

user_obj1, user_obj2 = [x for x in UserMemLeak.token._storage.keys()]
print(user_obj1)  # Still exists!
print(user_obj2)  # Still exists!
# This is a memory leak: the application does not need them, yet they are in memory because of a background util ref
print(sys.getrefcount(user_obj1))
print(sys.getrefcount(user_obj2))

print("\n-----")

class User:
    name = None
    token = LogDescriptor(use_weakrefs=True)

    def __repr__(self) -> str:
        return (f"<User object: {self.name}>")

    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} deleted")

john = User(name='John')
marry = User(name='Marry')
john.token = 'foo'
marry.token = 'baz'
print(User.token._storage.keyrefs())
del john
del marry
print(User.token._storage.keyrefs())  # empty: the weakref dict did not keep the objects alive

print("\n=====")
print("Script is about to exit...")
# alice and bob are still retained by the descriptor dictionaries (and by user_obj1/user_obj2).
# They remain alive until those strong references disappear.
# In this script, that happens during interpreter shutdown.