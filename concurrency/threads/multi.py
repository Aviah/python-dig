import random
import threading
import time


def increase_counter(sec, counter_increments):
    global counter
    global results
    for _ in range(counter_increments):
        c = counter + 1
        time.sleep(sec)
        counter = c
        results.append(c)
        # print(f"{threading.current_thread().name} incremented +1, sleep ({r:0.2f})")


def run_threads(sec_min, sec_max, counter_increments, print_results=False):
    global counter
    global results

    n = 3
    print(f"Running 10 threads each time, {n} times, counter increments per thread: {counter_increments}")
    for _ in range(n):
        counter = 0
        results = []
        th = [
            threading.Thread(target=increase_counter, args=(random.uniform(sec_min, sec_max), counter_increments))
            for _ in range(10)
        ]
        [t.start() for t in th]
        [t.join() for t in th]
        if print_results:
            print(f"Counter reached {counter}: {results}")

print("\n===== Threads: sec_min 0.0001, sec_max 0.0002 =====")
run_threads(0.0001, 0.0002, 20, True)
print("\n===== Threads: sec_min 0.01, sec_max 0.02 =====")
run_threads(0.01, 0.02, 10, True)
print("\n===== Threads: sec_min 0.0001, sec_max 0.0002 =====")
run_threads(0.0001, 0.0002, 5, True)
print("\n===== Threads: sec_min 0 sec_max 0 =====")
# Note: 0 secs still use the sleep system call
print("No real concurrency: Each thread finishes the increment before the next one is created")
run_threads(0, 0, 1, True)
