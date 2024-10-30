import multiprocessing as mp

import time


def answer(sec):
    print("Process says: Enter process\n", end='')
    print("Process says: The answer is\n", end='')
    time.sleep(sec)
    print("Process says: 42")
    print("Process says: Exit process\n", end='')


p = mp.Process(target=answer, kwargs={'sec': 2})
print("Start process...\n", end='')
p.close()
try:
    p.start()
except ValueError as e:
    print(e)  # process object is closed

p = mp.Process(target=answer, kwargs={'sec': 2})
p.start()
print("Stated...")
try:
    p.close()
except ValueError as e:
    print(e)  # Cannot close a process while it is still running. You should first call join() or terminate().
print("Not done yet...\n", end='')
p.join()  # Wait until the process  finished and "joined" the main
print(f"Done with exit code {p.exitcode}. Is alive: {p.is_alive()}")
p.close()
print("Closed!")
