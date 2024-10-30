import multiprocessing as mp
import datetime

N = 32


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


def worker(tasks):
    while True:
        try:
            task = tasks.get_nowait()
        except tasks.Empty:
            return
        result = fib(task)
        print(f"Process {mp.current_process().pid}: fibonacci of {task} is {result}\n", end='')


# Batch job, put everything beforehand
tasks = mp.Queue()
for n in range(N):
    tasks.put(n)

# Run until all tasks are done, no task is added once the job starts
started_on = datetime.datetime.now()
with mp.Pool(processes=5) as pool:
    for n in range(N):
        result = pool.apply_async(worker, args=(tasks,))

    pool.close()
    pool.join()

duration = datetime.datetime.now() - started_on
print(f"Done with process pool, took {duration.total_seconds()} seconds")  # Typically ~0.5 second

print("=====")
started_on = datetime.datetime.now()

for n in range(N):
    result = fib(n)
    print(f"Fibonacci of {n} is {result}\n", end='')

duration = datetime.datetime.now() - started_on
print(f"Done without processes, took {duration.total_seconds()} seconds")  # Typically ~+1 second
