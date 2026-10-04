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


print("----- Equality -----")
a3 = Account(123, 'John Doe', 100.5)
a4 = Account(123, 'John Doe', 100.5)
assert a3 == a4  # supports eq by attributes
assert a3 is not a4
print(a3)
print(a4)
print(a3 == a4)

print("\n===== Validation =====")
@dataclasses.dataclass
class AccountWithValidation(Account):
    def __post_init__(self):
        for field in dataclasses.fields(self):
            v_type = type(getattr(self, field.name))
            if v_type != field.type:
                raise TypeError(f"Wrong type for field <{field.name}>: expected {field.type}, got {v_type}")


try:
    m = AccountWithValidation("foo", "baz", 123.456)
except TypeError as e:
    print(repr(e))


print("\n===== Create dynamically =====")
AClass = dataclasses.make_dataclass(
    cls_name='AClass',
    fields=[('x', int), ('msg', str)],
    namespace={'mult_it': lambda self, x: self.x * x, 'say_hi': lambda self: print(self.msg)},
)

print(AClass)
assert dataclasses.is_dataclass(AClass)
a = AClass(100, 'greetings')
print(a.mult_it(2))
a.say_hi()

print("\n===== Defaults =====")
# The generated __init__ keeps order of fields and map them to __init__ parameters
# So fields with defaults should be last
try:
    @dataclasses.dataclass
    class BClass:
        foo: str = 'baz'
        spam: str  # fails, non default after default arg

except Exception as e:
    print(f"Error: {e}")


@dataclasses.dataclass
class BClass:
    spam: str  # works
    foo: str = 'baz'

print("\n===== Frozen =====")
@dataclasses.dataclass(frozen=True)
class CustomClass:
    foo: int
    bar: str

c = CustomClass(foo=1, bar='abc')
try:
    c.foo = 2  # excepts, frozen
except dataclasses.FrozenInstanceError as e:
    print(repr(e))



print("\n===== Kw only =====")
@dataclasses.dataclass(kw_only=True)
class CustomClass:
    foo: int
    bar: str

try:
    c = CustomClass(1, 2)  # excepts kw_only
except TypeError as e:
    print(repr(e))


print("\n===== Inheritance =====")

# fails
@dataclasses.dataclass
class CClass:
    spam: str = 'eggs'

try:

    @dataclasses.dataclass
    class DClass(CClass):
        """
        fails, inherited fields come before the parent
        so 'foo' w/o a default appears *after* parent's 'spam' that has a default
        """

        foo: str

except Exception as e:
    print(repr(e))

# works
@dataclasses.dataclass(kw_only=True)
class CClass:
    spam: str = 'eggs'

@dataclasses.dataclass
class DClass(CClass):
    foo: str
