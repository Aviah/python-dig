import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def using_foo():
    global lock_foo
    global lock_bar
    print(f"Entered {threading.current_thread().name}\n", end='')
    with lock_foo as lock:  # blocking
        print(f"Acquired foo: {lock}, waiting for bar...")
        time.sleep(1)
        print(f"Trying to acquire bar from {threading.current_thread().name}")
        tries = 0
        while not lock_bar.acquire(blocking=False):  # non-blocking
            tries += 1
            time.sleep(0.2)
            print(f"Failed to acquire bar on the {tries} try")
        print(f"Acquired  bar from {threading.current_thread().name}")
        print("Got bar! Good bye")


def using_bar():
    global lock_foo
    global lock_bar
    print(f"Entered {threading.current_thread().name}\n", end='')
    with lock_bar:  # blocking
        print(f"Acquired  bar from {threading.current_thread().name}")
        time.sleep(2)
    print(f"Released  bar from {threading.current_thread().name}")


threading.Thread(target=using_foo).start()
threading.Thread(target=using_bar).start()
