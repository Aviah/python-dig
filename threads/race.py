import threading
import time
from functools import partial


def atm(sec):
    global balance
    if balance >= 100:
        time.sleep(sec)  # Counting money
        balance -= 100
        print(f"{balance}\n", end='')


immediate = partial(atm, 0)
with_sleep = partial(atm, 1)

balance = 1000
for i in range(11):
    threading.Thread(target=immediate).start()  # OK, works

print("=====")
balance = 1000
for i in range(11):
    threading.Thread(target=with_sleep).start()  # Fails
