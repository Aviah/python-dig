# https://www.youtube.com/watch?v=0oTh1CXRaQ0
from pathlib import Path

# Since Python pulls the module from sys.modules,
# the module can manipulate sys.modules and replace itself with another module
import switch_package

print(switch_package)
import cpackage
from switch_package import cool
from switch_package.bloop import pitch

other_path = Path(__file__).parent / 'all_package'
cpackage.bloop.__path__.append(other_path.as_posix())
from cpackage.bloop.utils import oops

print(oops())
