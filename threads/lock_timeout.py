import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def using_foo():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}\n", end='')
    with lock_foo as lock:
        print(f"Acquired foo: {lock}")
        time.sleep(1)
        print("Waiting for bar...")
        lock = lock_bar.acquire(timeout=1)
        # lock = lock_bar.acquire(timeout=4)
        if not lock:
            print(f"Timed out: {lock}. Good bye!")
        else:
            print(f"Got the lock! {lock}. Good bye!")


def using_bar():
    global lock_bar
    print(f"Enter {threading.current_thread().name}\n", end='')
    with lock_bar:
        print("Acquired  bar...")
        time.sleep(3)


threading.Thread(target=using_bar).start()
threading.Thread(target=using_foo).start()
