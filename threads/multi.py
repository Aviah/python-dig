import random
import threading
import time

counter = 0
results = []


def increase_counter(sec, times):
    global counter
    global results
    for _ in range(times):
        c = counter + 1
        time.sleep(sec)
        counter = c
        results.append(c)
        # print(f"{threading.current_thread().name} incremented +1, sleep ({r:0.2f})")


def run_threads(sec_min, sec_max, times, print_results=False):
    global counter
    global results
    for _ in range(3):
        counter = 0
        results = []
        print("Counter Reset")
        th = [
            threading.Thread(target=increase_counter, args=(random.uniform(sec_min, sec_max), times))
            for _ in range(10)
        ]
        [t.start() for t in th]
        [t.join() for t in th]
        print(f"Counter final is: {counter}")
        if print_results:
            print(results)


run_threads(0.0001, 0.0002, 10000, False)
print("=====")
run_threads(0.01, 0.02, 100, False)
print("=====")
run_threads(0.0001, 0.0002, 1, True)
