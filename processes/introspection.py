import multiprocessing as mp
import time


def just_a_process():
    print("Enter process...\n", end='')
    print(f"My name is: {mp.current_process().name}")
    print(f"My pid is: {mp.current_process().pid}")
    print(f"Created as {mp.get_context()}")
    time.sleep(2)
    print("Exit process\n", end='')


p = mp.Process(target=just_a_process)  # can provide custom name arg here
p.start()
print(f"It's name is: {p.name}")
print(f"It is {p.pid}")
print(f"Alive: {p.is_alive()}")
print(f"Daemon: {p.daemon}")
p.join()
print(f"Alive: {p.is_alive()}")
p.close()
print(p)


print("=====")
p1 = mp.Process(target=just_a_process)
p2 = mp.Process(target=just_a_process)
p3 = mp.Process(target=just_a_process)
[x.start() for x in [p1, p2, p3]]
[x.join() for x in [p1, p2, p3]]
[x.close() for x in [p1, p2, p3]]
