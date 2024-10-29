import queue
import random
import threading
import time

withdrawal_queue = queue.Queue()
stop = threading.Event()


def atm():
    global balance
    global withdrawal_queue
    # print(f"Enter {threading.current_thread().name}")
    withdrawal_queue.put(-100)
    print(f"request -100\n", end='')


def atm_worker():
    global balance
    global stop
    global withdrawal_queue
    print("Enter worker...")
    print(f"Start worker, queue has {withdrawal_queue.qsize()} pending tasks.")
    while True:
        time.sleep(random.uniform(0.5, 1))
        try:
            request = withdrawal_queue.get(timeout=1)
        except queue.Empty:
            if stop.is_set():
                print("The tasks queue is empty, and received a stop event. Good bye!")
                return
            continue
        if balance > 0:
            balance += request
            print(
                f'Withdrawal done, balance is {balance}. Queue has {withdrawal_queue.qsize()} pending tasks.\n',
                end='',
            )
        else:
            print(
                f"Not enough balance, request refused. Queue has {withdrawal_queue.qsize()} pending tasks.\n",
                end='',
            )
        withdrawal_queue.task_done()


balance = 1000

# Worker thread (consumer)
t_worker = threading.Thread(target=atm_worker)
t_worker.daemon = True
t_worker.start()

# Create threads that put tasks (producers)
active_threads = []
for i in range(20):
    t_atm = threading.Thread(target=atm)
    active_threads.append(t_atm)
    time.sleep(random.uniform(0.2, 0.4))
    t_atm.start()

[t.join() for t in active_threads]
stop.set()
t_worker.join()
print(f"Done! The end balance is {balance}")
