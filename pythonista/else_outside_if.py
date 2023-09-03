x = 5
n = 5
for i in range(n):
    if i == x:
        break
else:
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
    print(f"{n} was kept in the while loop (the loop was not interrupted)")


i, n = 0, 6
while i < n:
    i += 1
    if i == 5:
        break
else:
    print(f"{n} was kept in the while loop (the loop was not interrupted)")


try:
    assert 2 == 2
except Exception:
    pass
else:
    # Safer in case an exception was wrongly ignored
    print("Do something only if (a) no exception* happened,  and (b) before the finally clause")
finally:
    print("Finally clause")
print("Do something (a) after finally, and (b) it's possible that an exception handler continued the flow")


def foo(x):
    try:
        return int(x)
    except Exception as e:
        print(repr(e))
    else:
        # left the try clause with return - else clause is skipped
        assert False
    finally:
        print("Bye bye")


def find(seq, target):
    for element in seq:
        if element == target:
            break
    else:
        # no break
        return -1
    return element


foo('abc')
print(foo('123'))
s = ['bar', 'baz', 'spam', 'eggs']
assert find(s, 'woo') == -1
assert find(s, 'spam') == 'spam'
