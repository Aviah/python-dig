import queue
import random
import multiprocessing as mp
import time


def atm(withdraw_queue):
    print(f"Entered {mp.current_process().name}, pid {mp.current_process().pid}")
    for _ in range(2):
        withdraw_queue.put(-100)
        print(f"pid  {mp.current_process().pid} requested -100\n", end='')
        time.sleep(random.uniform(0.2, 1))


def atm_worker(balance_info, withdraw_queue, stop, lock):
    print(f"Entered worker, pid {mp.current_process().pid} ...")
    print(f"Worker starting it's loop... Tasks on queue: {withdraw_queue.qsize()}")
    while True:
        try:
            time.sleep(random.uniform(0.1, 0.3))
            request = withdraw_queue.get(timeout=1)
        except queue.Empty:
            if stop.is_set():
                print(f"Queue is empty, received a stop event. Good bye from PID: {mp.current_process().pid}!")
                return
            continue
        with lock:
            print(f"Lock acquired by {mp.current_process().pid}")
            balance = balance_info['balance']
            if balance > 0:
                time.sleep(1)
                balance_info['balance'] += request
                balance_info['total_withdrew'] -= request
                print(
                    f'Withdraw done. Balance is: {balance}, remaining requests: {withdraw_queue.qsize()}\n',
                    end='',
                )
            else:
                print(
                    f"Not enough balance, request refused. Queue has {withdraw_queue.qsize()} pending tasks.\n",
                    end='',
                )

if __name__ == '__main__':

    with mp.Manager() as pman:
        withdraw_queue = pman.Queue()
        stop = pman.Event()
        balance_info = pman.dict()
        balance_info['balance'] = 300
        balance_info['total_withdrew'] = 0
        # This is a threading.lock proxy: supports context manager, acquire, timeout etc
        request_lock = pman.Lock()


        # Worker process (consumer)
        for _ in range(3):
            p_worker = mp.Process(target=atm_worker, args=(balance_info, withdraw_queue, stop, request_lock))
            p_worker.daemon = True
            p_worker.start()
            time.sleep(1)
        # Create processes that put tasks (producers)
        active_processes = []
        for i in range(4):
            p_atm = mp.Process(target=atm, args=(withdraw_queue,))
            active_processes.append(p_atm)
            time.sleep(random.uniform(0.2, 0.4))
            p_atm.start()

        [p.join() for p in active_processes]
        [p.close() for p in active_processes]
        stop.set()
        p_worker.join()
        p_worker.close()
        print(f"Balance is {balance_info}")
        print("Done!")
