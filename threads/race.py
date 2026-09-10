import threading
import time
from functools import partial


def atm(sec):
    global balance
    if balance >= 100:
        print("Prrrr...... dispensing....")
        if sec:
            # Avoid the sleep call even for 0 secs
            time.sleep(sec)
        balance -= 100


immediate = partial(atm, 0)
with_sleep = partial(atm, 1)

balance = 300
threads = []
for i in range(5):
    t = threading.Thread(target=immediate)# OK, works
    threads.append(t)
    t.start()
[t.join() for t in threads]
print(f"Done immediate. The balance is: {balance}")

# With sleep
# While sleeping, another thread managed to get the balance
balance = 300
threads = []
for i in range(5):
    t = threading.Thread(target=with_sleep)
    threads.append(t)
    t.start()
[t.join() for t in threads]
print(f"Done with sleep. The balance is: {balance}")
