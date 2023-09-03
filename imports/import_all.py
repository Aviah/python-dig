import sys

from npackage import *

a = AClass()
b = BClass()
print(a)
print(b)
print(api)  # module name includes the package
print(sys.modules['npackage.api'])
from npackage.api import ops

print(ops)
from npackage.api.ops import *

print(double_and_add(1, 100))
print(ops.say_hi())  # was not imported with *


import everything_package

print(everything_package.double_and_mult(10, 5))
print(everything_package.say_hello())


from all_package import *

print(travel())
print(answer())
