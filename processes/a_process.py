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
p.start()
print("Not done yet...\n", end='')
p.join()  # Wait until the process  finished and "joined" the main
print(f"Done with exit code {p.exitcode}. Is alive: {p.is_alive()}")
p.close()
