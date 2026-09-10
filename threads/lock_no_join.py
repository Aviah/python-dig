# Similar to lock.py, without the join for the Atm threads
# atm are started first, and withdraw first

import threading
import time

withdraw_lock = threading.Lock()


def atm(sec):
    global balance
    print(f"Entering Atm thread {threading.get_ident()}. Balance: {balance}\n", end='')
    with withdraw_lock:
        print(f"Lock acquired by Atm thread {threading.get_ident()}. Balance: {balance}\n", end='')
        if balance >= 100:
            print(f"Atm {threading.get_ident()} has enough balance. Balance: {balance}\n", end='')
            print(f"Prrrrrr.... dispensing .... {threading.get_ident()}")
            time.sleep(sec)
            balance -= 100
            print(f"Withdrew Atm {threading.get_ident()}. Balance: {balance}")
        else:
            print(f"Not enough balance in {threading.get_ident()}")


active_threads = []
balance = 400
for i in range(3):
    t = threading.Thread(target=atm, args=(0.5,))
    active_threads.append(t)
    t.start()

# Same as lock.py, but doesn't wait for the threads to join
# [t.join() for t in active_threads]


def another_atm(sec):
    global balance
    print(f"Entering Another-Atm thread {threading.get_ident()}. Balance: {balance}\n", end='')
    with withdraw_lock:
        print(f"Lock acquired by Another-Atm thread {threading.get_ident()}. Balance: {balance}\n", end='')
        if balance >= 100:
            print(f"Another Atm {threading.get_ident()} has enough balance. Balance: {balance}\n", end='')
            print(f"Prrrrrr.... dispensing .... {threading.get_ident()}")
            time.sleep(sec)  # Counting money
            balance -= 100
            print(f"Withdrew Another-Atm {threading.get_ident()}. Balance: {balance}")
        else:
            print(f"Not enough balance in {threading.get_ident()}")


for i in range(3):
    t1 = threading.Thread(target=another_atm, args=(0.5,))
    active_threads.append(t1)
    t1.start()

time.sleep(3)
print(f"Finished. Balance is {balance}. Done!")
