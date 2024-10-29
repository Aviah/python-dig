import datetime
import queue
import threading
import urllib.request
import tempfile
import shutil

tasks = queue.Queue()
N = 32


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def worker():
    global tasks
    while True:
        try:
            task = tasks.get(block=False)
        except queue.Empty:
            return
        result = fib(task)
        print(f"Fibonacci of {task} is {result}\n", end='')
        tasks.task_done()


# Batch job, put everything beforehand
for n in range(N):
    tasks.put(n)

# Run until all tasks are done, no task is added once the job starts
active_threads = []
started_on = datetime.datetime.now()
for _ in range(N):
    t = threading.Thread(target=worker)
    active_threads.append(t)
    t.start()

tasks.join()
duration = datetime.datetime.now() - started_on
print(f"Done with threads, took {duration.total_seconds()} seconds")  # Typically ~1 second

print("=====")
started_on = datetime.datetime.now()

for n in range(N):
    result = fib(n)
    print(f"Fibonacci of {n} is {result}\n", end='')

duration = datetime.datetime.now() - started_on
print(f"Done without threads, took {duration.total_seconds()} seconds")  # Typically ~1 second
