import threading
import time


def just_a_thread():
    print("\n# Entered thread...\n", end='')
    print(f"# My name is: {threading.current_thread().name}")
    print(f"# My id is {threading.get_ident()}")
    time.sleep(2)
    print(f"# I'm done! Bye from {threading.get_ident()}\n", end='')

print("\n===== Starting a thread =====")
t = threading.Thread(target=just_a_thread)  # can provide custom name arg here
t.start()
print(f"It's name is: {t.name}")
print(f"It's thread id is {t.ident}")
print(f"Is alive: {t.is_alive()}")
print(f"Is daemon: {t.daemon}")

t.join()
print(f"\nIs alive after join: {t.is_alive()}")

