import threading
import time


class AppThread(threading.Thread):
    def __init__(self, name, sec):
        super().__init__()
        self.name = name
        self.sec = sec

    def run(self):
        print(f"Start {self.name} from subclass...")
        print(f"I am {threading.current_thread().name}")
        time.sleep(self.sec)
        print(f"Exit {self.name}")


foo = AppThread('foo', 3)
bar = AppThread('bar', 1)
foo.start()
bar.start()
