import threading
import time


def some_thread():
    print("Hi")
    time.sleep(1)


t = threading.Thread(target=some_thread)
t.start()
t.join()
t.start()  # RuntimeError: threads can only be started once
