import queue
import threading
import time

withdraw_queue = queue.Queue()


def put_request():
    global balance
    global withdraw_queue
    time.sleep(0.2)
    withdraw_queue.put(-100)
    print(f"Put on queue: request to withdraw 100\n", end='')
    print(f"Requests on queue: {len(withdraw_queue.queue)}")


active_threads = []

def run_requests():
    global balance
    global withdraw_queue
    print(f"Thread {threading.get_ident()} started...")
    time.sleep(0.3)
    while withdraw_queue.queue:
        print(f"Queue has requests, requests on queue: {withdraw_queue.qsize()}")
        request = withdraw_queue.get()
        print(f"Got request, remaining requests on queue: {withdraw_queue.qsize()}")
        balance += request
        print(f'Balance updated: {balance}\n', end='')
        withdraw_queue.task_done()
    print(f"Good bye from {threading.get_ident()}!")
balance = 300
for i in range(3):
    t_atm = threading.Thread(target=put_request)
    active_threads.append(t_atm)
    t_atm.start()

t_rw = threading.Thread(target=run_requests)
active_threads.append(t_rw)

t_rw.start()
[t.join() for t in active_threads]
withdraw_queue.join()
print(f"Done. The balance is: {balance}")
