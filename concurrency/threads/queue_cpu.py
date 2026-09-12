import datetime
import queue
import threading

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
print(f"===== Calculate Fibonacci {N} with multiple threads, each calculatess a single number =====")
active_threads = []
started_on = datetime.datetime.now()
for _ in range(N):
    t = threading.Thread(target=worker)
    active_threads.append(t)
    t.start()

# Waiting for all tasks that were put on the queue to call task_done()
tasks.join()
threads_duration = datetime.datetime.now() - started_on
print(f"Done after {threads_duration}")

print(f"\n===== Calculate Fibonacci {N} sequentially in a loop =====")
started_on = datetime.datetime.now()

for n in range(N):
    result = fib(n)
    print(f"Fibonacci of {n} is {result}\n", end='')

seq_duration = datetime.datetime.now() - started_on
print(f"Done after {seq_duration}")
print("\n===== Results for CPU bound tasks =====")
print(f"With threads: {threads_duration}")
print(f"Sequentially in a loop: {seq_duration}")
