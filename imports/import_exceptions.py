try:
    import module_with_error
except Exception as e:
    print(repr(e))

try:
    from cpackage import spam
except ImportError:
    print("Import error, no module")

try:
    import cpackage.spam
except ModuleNotFoundError:
    print("Module not found error")

try:
    import missing
except ModuleNotFoundError:
    print("Module not found error")
