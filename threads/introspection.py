import threading
import time


def just_a_thread():
    print("Enter thread...\n", end='')
    print(f"My name is: {threading.current_thread().name}")
    print(f"I am {threading.get_ident()}")
    time.sleep(2)
    print("Exit thread\n", end='')


t = threading.Thread(target=just_a_thread)  # can provide custom name arg here
t.start()
print(f"It's name is: {t.name}")
print(f"It is {t.ident}")
print(f"Alive: {t.is_alive()}")
print(f"Daemon: {t.daemon}")
t.join()
print(f"Alive: {t.is_alive()}")


print("=====")
threading.Thread(target=just_a_thread).start()
threading.Thread(target=just_a_thread).start()
threading.Thread(target=just_a_thread).start()
