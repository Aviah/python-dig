import sys
from pathlib import Path

sys.path.append(Path(__file__).parent.parent.as_posix())
import apackage

sys.modules[__name__] = apackage
print(f"{__name__} imported")
