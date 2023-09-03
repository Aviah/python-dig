import json
import sys

print(f"Current module {sys.modules[__name__]}")
print("=====")
print(json)
print(type(json))
assert hasattr(json, '__dict__')
print(json.__package__)
assert json.__name__ not in sys.builtin_module_names
assert json.__name__ in sys.stdlib_module_names
print(json.__file__)

print("=====")
import itertools

print(itertools)
print(type(itertools))
assert itertools.__name__ in sys.builtin_module_names
assert itertools.__name__ in sys.stdlib_module_names

print("=====")
import types

m = types.ModuleType('mymodule')
print(m)
print(vars(m))

print("=====")
try:
    from . import bloop
except ImportError:
    print(". is not part of a package")
__package__ = 'cpackage'  # now it does
from . import bloop

print(bloop.__path__)

print("=====")
import importlib

print(__import__)  # should by used by Python
apackage = importlib.import_module('apackage')
print(apackage)
print(apackage.__package__)
print(apackage.__path__)
print(apackage.__file__)
from apackage import bloop

print(bloop)

print("=====")
cool = importlib.import_module('bpackage.cool')
print(cool)
print(cool.__package__)
print(cool.__file__)
assert not hasattr(cool, '__path__')  # only for packages

print("=====")
api = importlib.import_module('.api', package='mpackage')
print(api)
print(api.__package__)
print(api.__path__)
print(api.__file__)

print("=====")
foo = importlib.import_module('foo')
print(foo)
assert not foo.__package__  # not a package, empty string
assert not hasattr(foo, '__path__')  # not a package, only for packages
print(foo.__file__)
