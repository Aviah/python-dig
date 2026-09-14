# Fibonacci calculation tasks using a *joinable* queue

from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import datetime
import multiprocessing as mp
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
            result = fib(task)
            print(f"Process {mp.current_process().pid}: fibonacci of {task} is {result}\n", end='')
        except queue.Empty:  # the manager queue is a proxy, get the direct exception
            return
        finally:
            tasks.task_done()

def do_something():
    time.sleep(2)

if __name__ == '__main__':

    with mp.Manager() as m:

        tasks = m.JoinableQueue()
        for n in range(N):
            tasks.put(n)

        started_on = datetime.datetime.now()
        with ProcessPoolExecutor(max_workers=10) as ppe:
            fib_futures = [ppe.submit(worker, tasks=tasks) for _ in range(10)]
            other_futures = [ppe.submit(do_something) for _ in range(20)]
            # This is just for the demo. If the scenario is really simple w/o real queue & consumers,
            # can just wait for some of the futures: wait(fib_futures)
            tasks.join()
            print("The Fibonacci calculations work is done")
            fib_duration = datetime.datetime.now() - started_on
            print("Waiting for other work currently running on the pool...")

        print("All work on the executor pool is done")
        ppe_duration = datetime.datetime.now() - started_on

    print(f"Duration for fib tasks: {fib_duration}")
    print(f"Total work duration of the process executor pool: {ppe_duration}")