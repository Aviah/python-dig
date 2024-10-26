import threading
import queue
import time

withdrawal_queue = queue.Queue()


def atm():
    global balance
    global withdrawal_queue
    time.sleep(0.5)
    withdrawal_queue.put(-100)
    print(f"request -100\n", end='')


def run_withdrawal():
    global balance
    global withdrawal_queue
    while balance > 0:
        request = withdrawal_queue.get()
        balance += request
        print(f'>>> balance {balance}\n', end='')
        withdrawal_queue.task_done()
    print(f"The balance reached zero, ignoring {len(withdrawal_queue.queue)} withdrawal requests. Good Bye!")


active_threads = []
balance = 1000
for i in range(15):
    t_atm = threading.Thread(target=atm)
    active_threads.append(t_atm)
    t_atm.start()

t_rw = threading.Thread(target=run_withdrawal)
active_threads.append(t_rw)

t_rw.start()
[t.join() for t in active_threads]
# withdrawal_queue.join()
# Will not get here with join: thread exited with pending requests
print(f"Done! The end balance is {balance}")
