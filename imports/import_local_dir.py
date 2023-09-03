import sys
from pathlib import Path

assert Path(__file__).parent.as_posix() in sys.path
import bar

assert 'bar' in sys.modules
