from concurrent.futures import ProcessPoolExecutor, as_completed
import datetime
import  multiprocessing as mp
from pprint import pp

N = 36

def init_process():
    print(f"Process {mp.current_process().pid} created")

def fib(n):
    if n <= 1:
        fib_value = n
    else:
        fib_value = fib(n - 1)[1] + fib(n - 2)[1]

    return n, fib_value


if __name__ == '__main__':

    results = {}
    for mw in (2, 10, 36):
        print(f"\nStarting with a pool of {mw} max workers...")
        futures = []
        ppe = ProcessPoolExecutor(max_workers=mw, initializer=init_process)
        started_on = datetime.datetime.now()
        with ppe as e:
            for n in range(N):
                f = e.submit(fib, n)
                futures.append(f)


            for f in as_completed(futures):
                n, fib_value = f.result()
                print(f"Fibonacci of {n} is {fib_value}\n", end='')

        ppe_duration = datetime.datetime.now() - started_on
        print(f"Done with pool of {mw} max workers after {ppe_duration}")
        results[f"Pool of {mw} max workers"] = ppe_duration

    print("\n===== Results =====")
    pp(results)
