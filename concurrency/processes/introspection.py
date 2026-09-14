import multiprocessing as mp
import time


def just_a_process(foo):
    print("\n# Entered process...\n", end='')
    print(f"# My name is: {mp.current_process().name}")
    print(f"# My pid is: {mp.current_process().pid}")
    print(f"# Arg foo is: {foo}")
    print(f"# Context: {mp.get_context()}")
    time.sleep(2)
    print("# Exit process\n", end='')

if __name__ == '__main__':
    p = mp.Process(target=just_a_process, args=('bar',))  # can provide custom name arg here
    print(f"New process instance {id(p)}, pid is {p.pid}")
    print(p)
    p.start()
    print(p)
    print(f"The process instance {id(p)} has been started")
    print(f"It's name is: {p.name}")
    print(f"It's pid is: {p.pid}")
    print(f"Is alive: {p.is_alive()}")
    print(f"Daemon: {p.daemon}")
    p.join()
    print(f"Is alive: {p.is_alive()}")
    p.close()
    print(p)
