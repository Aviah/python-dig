import threading
import time

withdraw_lock = threading.Lock()

print("===== First ATM: Context manager =====")
def atm(sec):
    global balance
    with withdraw_lock:  # blocking
        if balance >= 100:
            print("Prrrrrr.... dispensing ....")
            time.sleep(sec)
            balance -= 100
            print(f"ATM: Your balance is {balance}\n", end='')


active_threads = []
balance = 300
print("Your starting balance is 300")
for i in range(5):
    t = threading.Thread(target=atm, args=(0.5,))
    active_threads.append(t)
    t.start()
[t.join() for t in active_threads]
print(f"Your final balance with lock context manager is: {balance}")


print("\n===== Another ATM: Manually acquire/release =====")
def another_atm(sec):
    global balance
    withdraw_lock.acquire()  # blocking by default
    if balance >= 100:
        print("Prrrrrr.... dispensing ....")
        time.sleep(sec)
        balance -= 100
        print(f"Another ATM: Your balance is {balance}\n", end='')
    # No context manager, no exception handling: Any exception will leave all withdrawals locked!
    # When manually acquire/release, add lock.release() in a finally clause
    withdraw_lock.release()


active_threads = []
balance = 300
print("Your starting balance is 300")
for i in range(5):
    t = threading.Thread(target=another_atm, args=(0.5,))
    active_threads.append(t)
    t.start()
[t.join() for t in active_threads]
print(f"Your final balance with explicit lock is: {balance}")


print("\n===== Careless ATM: No locks =====")
def careless_atm(sec):
    global balance
    # Forgot to use the lock...
    if balance >= 100:
        print("Prrrrrr.... dispensing ....")
        time.sleep(sec)
        balance -= 100
        print(f"Careless ATM: Your balance is {balance}\n", end='')


active_threads = []
balance = 300
print("Your starting balance is: 300")
for i in range(5):
    t = threading.Thread(target=careless_atm, args=(1,))  # Fails
    active_threads.append(t)
    t.start()
[t.join() for t in active_threads]
print(f"Your final balance with no lock is: {balance}. Oops!")

