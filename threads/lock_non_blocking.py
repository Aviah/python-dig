import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def using_foo():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}\n", end='')
    with lock_foo as lock:
        print(f"Acquired foo: {lock}, waiting for bar...")
        time.sleep(1)
        while not lock_bar.acquire(blocking=False):  # Can also use timeout
            time.sleep(0.2)
            print("Failed, still waiting")
        print("Got bar! Good bye")


def using_bar():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}\n", end='')
    with lock_bar:
        print("Acquired  bar...")
        time.sleep(2)


threading.Thread(target=using_foo).start()
threading.Thread(target=using_bar).start()
