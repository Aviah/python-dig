import queue
import random
import multiprocessing as mp
import time


def atm(withdrawal_queue):
    print(f"Enter {mp.current_process().name}, pid {mp.current_process().pid}")
    for _ in range(5):
        withdrawal_queue.put(-100)
        print(f"pid  {mp.current_process().pid} requested -100\n", end='')
        time.sleep(random.uniform(0.2, 1))


def atm_worker(balance_info, withdrawal_queue, stop):
    balance = balance_info['balance']
    print(f"Enter worker, pid {mp.current_process().pid} ...")
    print(f"Start worker, queue has {withdrawal_queue.qsize()} pending tasks.")
    while True:
        try:
            time.sleep(random.uniform(0.5, 1))
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
        # JoinableQueue allows task_done and join
        # withdrawal_queue.task_done()


withdrawal_queue = mp.Queue()
pman = mp.Manager()
stop = pman.Event()
balance_info = pman.dict()
balance_info['balance'] = 1000


# Worker process (consumer)
p_worker = mp.Process(target=atm_worker, args=(balance_info, withdrawal_queue, stop))
p_worker.daemon = True
p_worker.start()
time.sleep(5)
# Create processes that put tasks (producers)
active_processes = []
for i in range(4):
    p_atm = mp.Process(target=atm, args=(withdrawal_queue,))
    active_processes.append(p_atm)
    time.sleep(random.uniform(0.2, 0.4))
    p_atm.start()

[p.join() for p in active_processes]
[p.close() for p in active_processes]
stop.set()
p_worker.join()
p_worker.close()
print("Done!")
