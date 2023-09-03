import sys

import foo  # already imported and exists in sys.modules
import foobaz

print(foo)
assert 'baz' in sys.modules
try:
    print(baz)
except:
    print("baz was imported elsewhere, but not in this module namespace")

sys.modules[__name__].baz = sys.modules['baz']  # same like 'import baz' if it was already imported
print(baz)

# Note: Python applies a lock on the import,
# so even in a multithreaded app, the module code runs once after the first import
