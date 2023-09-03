import baz


def f():
    import baz  # already imported and exists in sys.modules

    print(baz)  # pulled from sys.modules, where it was saved after the first import
    import foo


f()
import foo  # already imported

f()  # already imported
print(foo)
