import multiprocessing as mp
import time


def answer(sec):
    print(f"# Process says: Entered process {mp.current_process().pid}\n", end='')
    for i in range(5):
        print(f"# For the {i} time, the answer is: 42")
        time.sleep(0.5)
    print("# Process says: Exit process\n", end='')

if __name__ == '__main__':
    print("===== Starting a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 2})
    print(f"New process instance {id(p)}, PID Is: {p.pid}")
    print(f"Closing before start...")
    p.close()
    try:
        print("Starting the process...")
        p.start()
    except ValueError as e:
        print(repr(e))  # process object is closed

    print("\n===== Closing a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 2})
    print(f"New process instance {id(p)}, pid is: {p.pid}")
    p.start()
    print(f"Started {id(p)}, pid is {p.pid}")
    try:
        p.close()
    except ValueError as e:
        print(e)  # Cannot close a process while it is still running. You should first call join() or terminate().
    print("Did not close. Not done yet...\n", end='')
    p.join()  # Wait until the process  finished and "joined" the main
    print(f"Done with exit code {p.exitcode}")
    print(f"Is alive: {p.is_alive()}")
    p.close()
    print("Closed!")

    print("\n===== Terminate a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 2})
    print(f"New process instance {id(p)}, pid is: {p.pid}")
    p.start()
    print(f"Started {id(p)}, pid is {p.pid}")
    time.sleep(0.5)
    print(f"Terminating process...")
    p.terminate()
    print(f"Is alive: {p.is_alive()}")
    p.join()
    print(f"Done with exit code {p.exitcode}")
    print(f"Is alive: {p.is_alive()}")
    p.close()
    print("Closed!")


    print("\n===== Kill a process =====")
    p = mp.Process(target=answer, kwargs={'sec': 2})
    print(f"New process instance {id(p)}, pid is: {p.pid}")
    p.start()
    print(f"Started {id(p)}, pid is {p.pid}")
    time.sleep(0.5)
    print(f"Killing the process...")
    p.kill()
    print(f"Is alive: {p.is_alive()}")
    p.join()
    print(f"Done with exit code {p.exitcode}")
    print(f"Is alive: {p.is_alive()}")
    p.close()
    print("Closed!")
