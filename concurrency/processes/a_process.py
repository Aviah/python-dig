import multiprocessing as mp

import time


def answer(sec):
    print("# Process says: Entered process\n", end='')
    print("# Process says: The answer is\n", end='')
    time.sleep(sec)
    print("# Process says: 42")
    print("# Process says: Exit process\n", end='')



if __name__ == '__main__':
    print("===== Start and close a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 2})
    print("Starting the process...\n", end='')
    p.start()
    time.sleep(0.1)
    print("Not done yet...\n", end='')
    print(f"Is alive: {p.is_alive()}")
    p.join()  # Wait until the process  finished and "joined" the main process
    print(f"Done. The exit code is: {p.exitcode}")
    print(f"Is alive: {p.is_alive()}")
    p.close()
    print("Closed!")

    print("\n===== Start and kill a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 5})
    print("Starting the process...\n", end='')
    p.start()
    time.sleep(0.5)
    p.kill()
    p.join()
    print(f"Killed. The exit code is: {p.exitcode}")
    print(f"Is alive: {p.is_alive()}")
