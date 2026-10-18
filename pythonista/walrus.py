# The walrus operator := provides a more elegant way to use assignments
# It's an assignment *expression*: The := binds a value *while that value is used in expression*
# But ultimately the walrus doesn't add functionality: It typically replaces a separate assignment line
# See: https://peps.python.org/pep-0572/

import random
import string

l1 = []
while (s:= sum(l1)) < 100:
    if s % 2 == 0:  # we don't have to compute the sum again
        print(f"Running sum is even: {s}")
    else:
        print(f"Running sum is odd: {s}")
    l1.append(random.randint(1, 20))

print(sum(l1))
print(l1)

print("\n=====")

chars = [random.choice(string.ascii_letters) for _ in range(1_000_000)]

def count_upper(seq):
    found = 0
    for element in seq:
        if ord('A') <= ord(element) <= ord('Z'):
            found += 1
    return found

if (upper_count := count_upper(chars)) > 500_000:  # saves one separate assignment
    print(f"More than half uppercases: {upper_count}")
else:
    print(f"More than half lowercases: {upper_count}")
