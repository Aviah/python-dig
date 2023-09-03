# https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader
# https://discuss.python.org/t/pep-690-lazy-imports-again/19661/33
import importlib.util
import sys

spec = importlib.util.find_spec('bar')
bar = importlib.util.module_from_spec(spec)
loader = importlib.util.LazyLoader(
    spec.loader
)  # https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader
print(bar)
loader.exec_module(bar)
print("-----")
print(bar.x)

print("=====")
spec = importlib.util.find_spec('apackage')
apackage = importlib.util.module_from_spec(spec)
loader = importlib.util.LazyLoader(spec.loader)
print(apackage)
loader.exec_module(apackage)
print("-----")  # w/o explict call to exec_module
print(apackage.__name__)
from apackage import cool

print(cool)
print(cool.__name__)
print(apackage.__name__)

assert 'bar' not in sys.modules
assert 'apackage' in sys.modules
assert 'cool' not in sys.modules
