import builtins
import sys
from importlib.util import find_spec

# Note:
# Running $ python -vv  myfile.py , will show all imports. This can be handy for debugging

# New in 3.4, for spec for module loaders
print(find_spec('itertools'))
print(find_spec('json'))
print(sys.meta_path)  # importers

# instead of
try:
    import blah
except ImportError:
    print(f"Error if blah is missing OR it fails to import other modules")
    import json

# use
if find_spec('blah'):
    try:
        import blah
    except ImportError:
        print("blah exists, it's an error in blah")
else:
    import json

print("=====")


def debug_import(name, *args, builtin_imp=builtins.__import__):
    print(f"Importing: {name}")
    return builtin_imp(name, *args)


builtins.__import__ = debug_import
import sqlite3
