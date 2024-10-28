import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def using_foo():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}")
    with lock_foo:
        print("Acquired foo, waiting for bar...")
        time.sleep(1)
        lock_bar.acquire()


def using_bar():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}")
    with lock_bar:
        print("Acquired  bar, waiting for foo...")
        lock_foo.acquire()


threading.Thread(target=using_foo).start()
threading.Thread(target=using_bar).start()
