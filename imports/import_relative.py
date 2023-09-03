# relative import is a *package context*, not a directory context
# https://docs.python.org/3/tutorial/modules.html#intra-package-references
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time

from mpackage.api import ops

print(ops.double_and_add_one(100))  # ops uses relative import, works


import bpackage
import foo

from . import bpackage  # fails, although relative import is used within the package
from . import foo  # will fail as well
