import importlib.util
import sys

import apackage
import bpackage  # The package's __init__ imports all modules

assert not hasattr(apackage, 'cool')
assert hasattr(bpackage, 'cool')

print(bpackage.__package__)
print(bpackage.cool)
print(importlib.util.find_spec('bpackage.cool'))
print(importlib.util.find_spec('apackage.cool'))  # found, but not imported

assert not 'apackage.cool' in sys.modules
from apackage import cool

assert hasattr(apackage, 'cool')
assert 'apackage.cool' in sys.modules

import cpackage

assert not hasattr(apackage, 'bloop')
assert hasattr(bpackage, 'bloop')  # bpackage __init__ imports modules under bloop, so bloop was added to sys.modules
assert hasattr(cpackage, 'bloop')

assert hasattr(cpackage.bloop, 'jump')
print(cpackage.bloop.jump)


print(cpackage.__path__)
print(cpackage.bloop.__path__)
from cpackage.bloop import jump

assert not hasattr(jump, '__path__')


"""Note: python supports "namespace" packages that allow to split a single app
to several subpackages, each can be installed separately, yet called from the same
app namespace"""
