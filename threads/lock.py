import threading
import time


withdrawal_lock = threading.Lock()


def atm(sec):
    global balance
    with withdrawal_lock:
        if balance >= 100:
            time.sleep(sec)  # Counting money
            balance -= 100
            print(f"atm: {balance}\n", end='')


active_threads = []
balance = 1000
for i in range(11):
    t = threading.Thread(target=atm, args=(0.5,))
    active_threads.append(t)
    t.start()

[t.join() for t in active_threads]


print("=====")
active_threads = []
balance = 1000


def another_atm(sec):
    global balance
    with withdrawal_lock:
        if balance >= 100:
            time.sleep(sec)  # Counting money
            balance -= 100
            print(f"Another atm: {balance}\n", end='')


for i in range(11):
    t1 = threading.Thread(target=atm, args=(1,))
    t2 = threading.Thread(target=another_atm, args=(0.5,))
    active_threads.append(t1)
    active_threads.append(t2)
    t1.start()
    t2.start()

[t.join() for t in active_threads]

print("=====")
# The lock is not enforced, unless the code is actually using it
balance = 1000
active_threads = []


def careless_atm(sec):
    global balance
    # Forgot to use the lock...
    if balance >= 100:
        time.sleep(sec)  # Counting money
        balance -= 100
        print(f"Careless atm: {balance}\n", end='')


for i in range(11):
    t1 = threading.Thread(target=atm, args=(1,))
    t2 = threading.Thread(target=careless_atm, args=(1,))  # Fails
    active_threads.append(t1)
    active_threads.append(t2)
    t1.start()
    t2.start()

[t.join() for t in active_threads]
print("Done!")
