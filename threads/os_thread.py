# Python thread is a native OS thread
import os
import subprocess
import threading
import time

def a_thread():

    print(f"Entering a thread...")
    print(f"Python id: {threading.get_ident()}")
    print(f"OS id: {threading.get_native_id()}")
    time.sleep(1)
    print(f"Bye bye from {threading.get_ident()}")

# Note: MacOS does not expose threads as "lightweight process" with their id
t1 = threading.Thread(target=a_thread)
t1.start()
print("OS threads of main process: 1")
subprocess.run(f"ps -M -p {os.getpid()}", shell=True)
t2 = threading.Thread(target=a_thread)
t2.start()
print("OS threads of main process: 2")
subprocess.run(f"ps -M -p {os.getpid()}", shell=True)
t1.join()
t2.join()
print("OS threads of main process: 0")
subprocess.run(f"ps -M -p {os.getpid()}", shell=True)




