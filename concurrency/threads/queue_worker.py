# A daemon worker thread

import queue
import random
import threading
import time

withdraw_queue = queue.Queue()
stop = threading.Event()


def atm():
    global balance
    global withdraw_queue
    print(f"Thread {threading.get_ident()} started...")
    withdraw_queue.put(-100)
    print(f"Put on queue: request to withdraw 100\n", end='')
    print(f"Requests on queue: {len(withdraw_queue.queue)}")


def atm_worker():
    global balance
    global stop
    global withdraw_queue
    print(f"Worker thread {threading.get_ident()} started...")
    print(f"Pending on queue: {withdraw_queue.qsize()}")
    while True:
        time.sleep(random.uniform(0.5, 1))
        try:
            request = withdraw_queue.get(timeout=1)
            print("Prrrrr..... dispensing...")
            time.sleep(0.1)
            balance += request
            print(f"Withdraw completed, balance is: {balance}")
        except queue.Empty:
            if stop.is_set():
                print("No pending requests. Received a stop event. Good bye!")
                return
            else:
                print("No pending requests. Waiting for new requests...")
            continue
        withdraw_queue.task_done()


balance = 300

# Worker thread (consumer)
t_worker = threading.Thread(target=atm_worker)
t_worker.daemon = True
t_worker.start()

# Create threads that put tasks (producers)
active_threads = []
for i in range(5):
    t_atm = threading.Thread(target=atm)
    active_threads.append(t_atm)
    time.sleep(random.uniform(0.2, 0.4))
    t_atm.start()

[t.join() for t in active_threads]
time.sleep(5)
stop.set()
t_worker.join()
print(f"Done. The balance is: {balance}")
