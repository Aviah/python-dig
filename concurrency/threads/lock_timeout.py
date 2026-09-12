import datetime
import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def using_foo():
    global lock_foo
    global lock_bar
    print(f"Entered {threading.current_thread().name}\n", end='')
    with lock_foo as lock:
        print(f"Acquired foo from {threading.current_thread().name}. The lock is: {lock}")
        time.sleep(1)
        print(f"{datetime.datetime.now().isoformat()} | Trying to acquire bar from {threading.current_thread().name}")
        lock = lock_bar.acquire(timeout=2)
        if not lock:
            print(f"{datetime.datetime.now().isoformat()} | Timed out. The lock is: {lock}. I'm done here.")
        else:
            print(f"Got the lock! The lock is: {lock}. Good bye!")


def using_bar():
    global lock_bar
    print(f"Enter {threading.current_thread().name}\n", end='')
    with lock_bar:
        print(f"Acquired  bar from {threading.current_thread().name}")
        time.sleep(4)


threading.Thread(target=using_bar).start()
threading.Thread(target=using_foo).start()
