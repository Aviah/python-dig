import threading
import time

should_run: bool = True


def wait_for_var():
    global should_run
    print("Hi there, starting...")
    while should_run:
        ...
    print("Good bye, I'm done!")


t = threading.Thread(target=wait_for_var)
t.start()
# t.join()
# Will never get here with join
time.sleep(2)
should_run = False
print("Got here")
