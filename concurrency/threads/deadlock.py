import threading
import time

lock_foo = threading.Lock()
lock_bar = threading.Lock()


def thread1():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}")
    with lock_foo:
        print("Acquired foo, waiting for bar...")
        time.sleep(1)
        lock_bar.acquire()


def thread2():
    global lock_foo
    global lock_bar
    print(f"Enter {threading.current_thread().name}")
    with lock_bar:
        print("Acquired  bar, waiting for foo...")
        time.sleep(1)
        lock_foo.acquire()


threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()
time.sleep(2)
print("Oops... the dreaded deadlock!")
