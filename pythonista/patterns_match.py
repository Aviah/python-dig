print("\n===== Match by literals =====")

def match_literal(x):
    match x:
        case 'foo':
            print('Matched foo')

        case 42:
            print('Matched 42')

        case 42.0:
            print('Matched 42.0')  # literals matched by equality, so 42 will match before

        case [1,2,3]:
            print('Matched [1,2,3]')

        case {'spam': 'eggs'}:
            print("Matched: {'spam': 'eggs'}")

        case _:
            print(f"Not matched: Wrong parameter")


match_literal('foo')
match_literal([1,2,3])
match_literal([1, 2, 3, 4])  # not matched, extra sequence elements are not allowed
match_literal(42)
match_literal(42.0)
match_literal({'spam': 'eggs'})
match_literal({'spam': 'eggs', 'bloop': 'jump'})  # matched, extra mapping keys are allowed


def match_instance(x):

    match x:
        case list():
            print('Matched list')

        case float():
            print('Matched float')

        case dict():
            print('Matched dict')

        case set():
            print('Matched set')

        case _:
            print('Not matched: Wrong type')


print("\n===== Match by instance of =====")

match_instance({'abc': 123})
match_instance(42)
match_instance(42.0)

class D(dict): pass
match_instance(D())


print("\n===== Match truthiness =====")
# True, False and None are matched by *identity*, not truthiness.

def match_truth(x):
    match x:
        case True:
            print ("The truth is out there")

        case False:
            print("Fake")

        case None:
            print("Nothing")

        case _:
            # Match does not auto-cast to bool
            print("Not matched")

match_truth(True)
match_truth(False)
match_truth(None)
match_truth([])
match_truth(0)
match_truth('')
match_truth(D())
match_truth(bool([1,2,3]))


print("\n===== Match with assignment =====")

def match_assign(x):

    match x:
        case[1, 2, p]:
            print(f"Starts with 1,2 and has any third item, len == 3: {p}")

        case [1, 2, *p]:
            print(f"Starts with 1,2: {p}")

        case {'spam': 'eggs', 'foo': p}:
            print(f"Has spam, foo, value of spam is eggs: {p}")

        case {'spam': _, 'foo': p}:
            print(f"Has spam, foo: {p}")

        case {'spam': p, **kwargs}:
            # kwargs contains only the unmatched keys; 'spam' is excluded.
            print(f"Has spam: {p}, {kwargs}")

        case [1, *p]:
            print(f"Starts with 1: {p}")

        case p:
            print(f"Catch all: {p}")

        # remaining clause unreachable - case p catches everything
        # case _:
        #    print("")

match_assign([100, 200, 300])
match_assign({'spam':'eggs', 'foo': 'POOL'})
match_assign({'spam': 'blah', 'foo': 'BLAH'})
match_assign([1, 2, 'Third'])
match_assign([1, 2, "Whoo", "Hoo"])
match_assign([1, "pool", "bloop", "blah"])
match_assign(1234)
match_assign({'spam': 'jump', 'baz': 'bar', 1234:1234})


print("\n===== Order matters =====")

def match_order_matters(x):
    """
    Broad patterns first can shadow more specific patterns below
    """

    match x:

        case [1, *p]:
            print(f"Starts with 1, {p}")

        case [1, 2, *p]:
            print(f"Starts with 1,2: {p}")

        case {'spam': _, 'foo': p}:
            print(f"Has spam, foo {p}")

        case {'spam': 'eggs', 'foo': p}:
            print(f"Has spam, foo, value of spam is eggs: {p}")

        case p:
            print(f"Catch all: Found {p}")

        # remaining clause unreachable - case p catches everything
        # case _:
        #    print("")

match_order_matters({'spam':'eggs', 'foo': 'EGGS'})  # will not get to "value of spam is eggs"
match_order_matters({'spam': 'blah', 'foo': 'BLAH'})
match_order_matters([1, 2, "Whoo", "Hoo"])  # will not get to "starts with 1,2"
match_order_matters([1, "pool", "bloop", "blah"])


print("\n===== Match with guards =====")

def match_guard(x):

    match x:
        case int() if x > 10:
            print(f"Matched int > 10")


        case float() if x > 100:
            print("Matched float > 100")

        case list() if len(x) > 2:
            print("Matched list where len > 2")

        case _:
            print(f"No match {x}")

match_guard(99.0)
match_guard(101)
match_guard(101.0)
match_guard([1, 2])
match_guard(['foo', 'spam', 'bar'])


print("\n===== Match dynamically in runtime=====")
# A bare name in a pattern is an assignment capture pattern, not a value comparison
# Use a dotted name for a value pattern.

class NS: pass

NS.a = 'foo'
NS.b = 1234
NS.c = {'spam': 'eggs'}

def match_ns(x):

    match x:
        case NS.a:  # Usage of .a prevents "assignment to a"
            print(f"Matched NS.a: {x}")

        case NS.b:
            print(f"Matched NS.b: {x}")

        case NS.c:
            print(f"Matched NS.c: {x}")

        case _:
            print(f"No match {x}")


match_ns('baz')
match_ns('foo')
match_ns({'spam': 'bloop'})
NS.c = {'spam': 'bloop'}
match_ns({'spam': 'bloop'})


print("\n===== Match OR =====")
def match_or(x):

    match x:
        case {'color': 'blue'} | {'color': 'red'}:
            print("Matched blue or red")

        case [1, p] | [2, p]:
            # OR alternatives should bind to the same name
            print(f"Matched starts with 1 or 2: {p}")

        case _:
            print(f"No match {x}")


match_or({'color': 'yellow'})
match_or({'color': 'blue'})
match_or([1, 'bloop'])
match_or([3, 'bloop'])

# See also
# https://peps.python.org/pep-0636/
# https://www.youtube.com/watch?v=ZTvwxXL37XI&t=100s