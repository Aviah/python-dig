print("===== Loops =====")

x = 5
n = 5
for i in range(n):
    if i == x:
        break
else:
    print("Loop exhausted")
    print(f"{n} was kept in the loop (the loop was not interrupted)")

n = 6
for i in range(n):
    if i == x:
        break
else:
    pass  # will not get here

i, n = 0, 5
while i < n:
    i += 1
else:
    print("Loop exhausted")
    print(f"{n} was kept in the while loop (the loop was not interrupted)")

i, n = 0, 6
while i < n:
    i += 1
    if i == 5:
        break
else:
    print("Loop not exhausted")


def find(seq, target):
    for element in seq:
        if element == target:
            break
    else:
        # no break
        print("Loop exhausted, not found")
        return -1
    return element


s = ['bar', 'baz', 'spam', 'eggs']
assert find(s, 'woo') == -1
assert find(s, 'spam') == 'spam'


print("\n===== Try except else =====")
# Nested try except with else
try:
    with open('../core/foo.txt') as f:
        content = f.read()
except Exception as e:
    # Handle file opening issues
    ...
else:
    # else enables to separate try-except clauses for different parts of the flow
    try:
        print("Processing the file...")
        int(content)
    except Exception as e:
        # Handle file processing issues, in a separate clause
        print("File processing failed")

try:
    int('1')
except ValueError:
    pass
else:
    # Keep code that is not handled by the except clause/s outside the try clause
    print("Do something before the finally clause, if no exception* happened")
finally:
    print("Entered finally clause")


def foo(x):
    try:
        return int(x)
    except Exception as e:
        print(repr(e))
    else:
        # left the try clause with return: the "else" clause is skipped
        assert False
    finally:
        print("Bye bye")

print(foo('123'))
print(foo('a'))

