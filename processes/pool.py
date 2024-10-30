import datetime
import multiprocessing as mp

N = 32


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


pool = mp.Pool(processes=5)
started_on = datetime.datetime.now()
result = pool.imap(fib, range(N))  # imap_unordered will be faster
for n, r in enumerate(result):
    print(f"Fibonacci of {n} is {r}\n", end='')


duration = datetime.datetime.now() - started_on
print(f"Done with process pool, took {duration.total_seconds()} seconds")  # Typically ~0.5 second
