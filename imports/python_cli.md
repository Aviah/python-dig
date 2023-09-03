# Try
```shell
python -m bpackage
python -m bpackage.cool
python  bpackage/bloop/jump.py
python  python -m mpackage.api.ops  # works
python  mpackage/api/ops.py  # fails
python  with_main  # will run the main file (also works for zip/egg files)
python -m site --user-base
python -m site --user-site  # pip install --user uses this
```


* The warning appears since when "python -m" tries to import it, the bpackage.__init__ already imported it
* Running w/o -m, the file is considered __main__
* Relative imports work in a package context (-m), and not in directory context
* -S will skip site import