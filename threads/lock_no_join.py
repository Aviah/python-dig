import threading
import time

withdrawal_lock = threading.Lock()


def atm(sec):
    global balance
    print(f"Entering atm, balance is {balance}...\n", end='')
    with withdrawal_lock:
        print(f"atm acquired lock {threading.get_ident()}: balance is {balance}\n", end='')
        if balance >= 100:
            time.sleep(sec)  # Counting money
            balance -= 100
            print(f"atm: {balance}\n", end='')
        else:
            print(f"No balance, but acquired the lock at atm thread {threading.get_ident()}")


active_threads = []
balance = 1000
for i in range(11):
    t = threading.Thread(target=atm, args=(0.5,))
    active_threads.append(t)
    t.start()

# Same as lock.py, but don't wait for the threads to join
# [t.join() for t in active_threads]


print("=====")
balance = 1100


def another_atm(sec):
    global balance
    print(f"Entering another atm, balance is {balance}...\n", end='')
    with withdrawal_lock:
        print(f"Another atm acquired lock {threading.get_ident()}, balance is {balance}\n", end='')
        if balance >= 100:
            time.sleep(sec)  # Counting money
            balance -= 100
            print(f"Another atm: {balance}\n", end='')


for i in range(5):
    t1 = threading.Thread(target=another_atm, args=(0.5,))
    active_threads.append(t1)
    t1.start()


[t.join() for t in active_threads]
print(f"Balance is {balance}. Done!")
