# Fibonacci calculation tasks using a queue

import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, as_completed
import datetime
import queue

N = 40


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def worker(tasks):
    while True:
        try:
            task = tasks.get_nowait()
        except queue.Empty:  # the manager queue is a proxy, get the direct exception
            return
        result = fib(task)
        print(f"Process {mp.current_process().pid}: fibonacci of {task} is {result}\n", end='')

if __name__ == '__main__':

    with mp.Manager() as m:

        tasks = m.Queue()
        for n in range(N):
            tasks.put(n)

        started_on = datetime.datetime.now()
        with ProcessPoolExecutor(max_workers=10) as ppe:
            futures =  [ppe.submit(worker, tasks=tasks) for _ in range(N)]
            [f.result() for f in as_completed(futures)]

        ppe_duration = datetime.datetime.now() - started_on
        print(f"Done with process executor pool: {ppe_duration}")

        print("\n ===== Sequentially in a loop =====")
        started_on = datetime.datetime.now()

        for n in range(N):
            result = fib(n)
            print(f"Fibonacci of {n} is {result}\n", end='')

        seq_duration = datetime.datetime.now() - started_on
        print(f"Done sequentially  in a loop: {seq_duration}")

    print(f"\n===== Results =====")
    print(f"With a pool of 10 max workers: {ppe_duration}")
    print(f"Sequentially in a loop: {seq_duration}")
