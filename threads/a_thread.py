import threading
import time


def answer(sec):
    print("Thread says: Enter thread\n", end='')
    print("Thread says: The answer is\n", end='')
    time.sleep(sec)
    print("Thread says: 42")
    print("Thread says: Exit thread\n", end='')


t = threading.Thread(target=answer, kwargs={'sec': 2})
print("Start thread...\n", end='')
t.start()
print("Not done yet...\n", end='')
t.join()  # Wait until the thread finished and "joined" the main thread
print("Done!")
