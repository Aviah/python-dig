import dataclasses


@dataclasses.dataclass
class Account:
    id: int
    name: str
    balance: float
    approved: bool = True


assert dataclasses.is_dataclass(Account)
print(Account.__annotations__)
a1 = Account(123, 'John Doe', 100.5)
print(a1)
assert dataclasses.is_dataclass(a1)
a2 = Account('Uncle Stan', 456.0, 10)
print(a2)  # no validation by default
a1.id = 789  # unlike named tuples
print(a1)
print([x for x in dataclasses.astuple(a1)])  # not iterable by default


a3 = Account(123, 'John Doe', 100.5)
a4 = Account(123, 'John Doe', 100.5)
assert a3 == a4  # support eq by attributes
assert a3 is not a4


@dataclasses.dataclass
class AccountWithValidation(Account):
    def __post_init__(self):
        for field_name, field_type in self.__annotations__.items():
            if type(getattr(self, field_name)) != field_type:
                raise TypeError(f"Wrong type for field {field_name}")


try:
    m = AccountWithValidation("foo", "baz", 123.456)
except TypeError as e:
    print(repr(e))


# create dataclasses dynamically
AClass = dataclasses.make_dataclass(
    'AClass',
    [('x', int), ('msg', str)],
    namespace={'mult_it': lambda self, x: self.x * x, 'say_hi': lambda self: print(self.msg)},
)

print(AClass)
assert dataclasses.is_dataclass(AClass)
a = AClass(100, 'greetings')
print(a.mult_it(2))
a.say_hi()

# like calling with args, defaults should be last
try:

    @dataclasses.dataclass
    class BClass:
        foo: str = 'baz'
        spam: str  # fails, non default after default arg

except Exception as e:
    print(f"Error: {e}")


print("=====")


@dataclasses.dataclass(kw_only=True, frozen=True)
class CustomClass:
    foo: int
    bar: str


c = CustomClass(foo=1, bar='abc')
try:
    c.foo = 2  # excepts, frozen
except dataclasses.FrozenInstanceError as e:
    print(repr(e))

try:
    c = CustomClass(1, 2)  # excepts, kw_only
except TypeError as e:
    print(repr(e))


print("=====")


# inheritance
@dataclasses.dataclass
class CClass:
    spam: str = 'eggs'


@dataclasses.dataclass
class DClass(CClass):
    """
    fails, dataclass has an ordered fields mapping by mro
    so 'foo' w/o a default, appears after parent's 'spam' that has a default
    """

    foo: str
