import os
import site
import sys
from pathlib import Path

print(sys.prefix)  # venv
print(sys.exec_prefix)  # venv
print(sys.base_prefix)  # machine
print(sys.base_exec_prefix)  # machine
print(sys.executable)  # which python
print((Path(sys.executable).parent.parent / 'pyvenv.cfg').is_file())  # if True, search venv site-packages
print(site.getsitepackages())
print(site.getuserbase())
print(site.getusersitepackages())  # pip install --user will install here
print([x for x in sys.path if x.endswith('site-packages')][0])
print("=====")
[print(x) for x in os.environ['PYTHONPATH'].split(':')]
assert all([x in sys.path for x in os.environ['PYTHONPATH'].split(':')])

"""
Customize site imports:
* Run python with  $ python -S   , skips site
* Can also skip env vars with -E, user site -s, or both -I (usefull to debug env issues)
* A sitecustomize module on the module search path, typically added by admins
* A usercustomize module on the module search path, typically added by the user
* The sitecustomize, usercustomize modules can use the 'site' module utils (like addsitedir)
* A .pth file with list of directories, saved in the site-packages dir
* Edit the PYTHONPATH
https://docs.python.org/3/library/site.html
https://docs.python.org/3/library/sys.html
https://docs.python.org/3/tutorial/modules.html#the-module-search-path

"""
