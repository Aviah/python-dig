# Threads do not have builtin kill

import threading
import time

stop = threading.Event()

def worker():

    print("Worker started...")
    c = 0
    while not stop.is_set():
        print(f"Still here! Counter is {c}")
        c += 1
        time.sleep(2)

    print("Bye bye!")


t = threading.Thread(target=worker)
t.start()
time.sleep(5)
print("Settings stop event...")
stop.set()
