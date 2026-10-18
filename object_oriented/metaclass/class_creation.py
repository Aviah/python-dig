"""
__prepare__: namespace created
Creates the namespace in which the class will execute.
It can pre-populate it or return a custom mapping.

__new__: class object created
Receives the completed namespace and can modify it before
the class object is created.

__init__: modifies the new class object
Receives the already-created class and can modify it in place.
"""

class Metaclass(type):

    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        print(f"Metaclass __prepare__ invoked: {name} | {bases} | {kwargs}")
        # can return a special kind of dict

        # Class keywords are passed separately to __prepare__, __new__, and __init__.
        # Here double_jump is used by __prepare__ and merely accepted/ignored
        # by __new__ and __init__.

        namespace = super().__prepare__(name, bases, **kwargs)
        namespace['bloop'] = 'jump'  # customizing the to-be-created class's namespace

        # Each metaclass hook receives its own kwargs dict.
        # Popping here does not affect the kwargs later passed to __new__ or __init__.
        if kwargs.pop('double_jump', False):
            namespace['bloop'] = 'jumpjump'

        print(namespace)

        # Note: When the final class object is created with __new__, namespace is *copied* into a new dict
        # Thus, if namespace is a special kind of dict: useful in the metaclass, but not once the class is created
        # https://docs.python.org/3/reference/datamodel.html#preparing-the-class-namespace
        return namespace

    def __new__(mcls, name, bases, attrs, **kwargs):
        """
        Creates the class object
        Can modify the class creation args before it's created
        """
        print(f"Metaclass __new__ invoked: {mcls} | {name} | {bases} | {attrs}")
        assert super().__new__ is type.__new__

        # In this demo the kwargs are treated as metaclass configuration.
        # Since __new__ does not forward them to type.__new__, they do not reach __init_subclass__.
        # see metaclass/subclass.py
        cls = super().__new__(mcls, name, bases, attrs)

        print(cls)  # cls was created
        if 'double_jump' in kwargs:
            # __prepare__ popped double_jump from its own kwargs dict: it's still available to other mcls hooks
            print("double_jump provided to metaclass")
        return cls

    def __init__(cls, name, bases, attrs, **kwargs):
        """
        Receives the created class: can modify
        Can modify it in place
        Returns None: the class object already exists"""
        print(f"Metaclass __init__ invoked: {cls} | {name} | {bases} | {attrs}")

        if 'double_jump' in kwargs:
            # __prepare__ popped double_jump from its own kwargs dict: it's still available to other mcls hooks
            print("double_jump provided to metaclass")

        # The **kwargs are for the metaclass itself
        # Forward **kwargs in metaclass __init__ only if the next metaclass in the mro is expected to consume them.
        # Here it's type, so we don't pass them
        super().__init__(name, bases, attrs)  # Conceptually type.__init__(cls, name, bases, attrs)


class AClass:
    pass


class BClass:
    pass


class CClass(AClass, BClass, metaclass=Metaclass):
    foo = 'bar'

    def spam(self):
        return f"{self.foo} eggs"

c = CClass()
print(c.spam())
print(c.bloop)

print("\n=====")

# Customize the class creation process with kwargs sent to and handled by the metaclass
class DClass(AClass, BClass, metaclass=Metaclass, double_jump=True):
    foo = 'pool'

    def spam(self):
        return f"{self.foo} eggs"

d = DClass()
print(d.spam())
print(d.bloop)