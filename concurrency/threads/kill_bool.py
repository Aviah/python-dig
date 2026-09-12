# Threads do not have builtin kill
import threading
import time

should_run: bool = True


def wait_for_var():
    global should_run
    print("Hi there, I'm just starting...")
    while should_run:
        ...
    print("Good bye, I'm done!")


t = threading.Thread(target=wait_for_var)
t.start()
# t.join()
# Will never get here with join
time.sleep(2)
print("Now setting should_run to False...")
should_run = False
print("Finished, should_run is off")
