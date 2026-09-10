import threading
import time


class AppThread(threading.Thread):
    def __init__(self, name, sec):
        super().__init__()
        self.name = name
        self.sec = sec
        print(f"Initialized {name}")

    def run(self):
        print(f"Start running! I am {self.name}, thread {threading.get_ident()}, an instance of {self.__class__.__name__}")
        time.sleep(self.sec)
        print(f"Still here... {threading.current_thread().name}")
        time.sleep(self.sec)
        print(f"Exit {self.name}")


foo = AppThread('foo', 3)
bar = AppThread('bar', 1)
foo.start()
bar.start()
print(f"foo is_alive: {foo.is_alive()}")
print(f"bar is_alive: {bar.is_alive()}")
time.sleep(5)
print(f"foo is_alive: {foo.is_alive()}")
print(f"bar is_alive: {bar.is_alive()}")