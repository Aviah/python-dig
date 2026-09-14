import time
import datetime
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp
from pprint import pp
from types import TracebackType


def work():
    time.sleep(5)
    return f"Submitted task done at {datetime.datetime.now().isoformat()} on PID: {mp.current_process().pid}"

class MyPPE(ProcessPoolExecutor):

    def __exit__(
        self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None
    ) -> bool | None:

        print(f"{datetime.datetime.now().isoformat()}: Exit the pool's context manager: __exit__")
        print(f"Shutting down the processes, wait to finish the running work...")
        super().__exit__(exc_type, exc_val, exc_tb)
        print(f"{datetime.datetime.now().isoformat()}: Context manager finished")


if __name__ == "__main__":
    with MyPPE(max_workers=3) as ppe:

        futures = [ppe.submit(work) for _ in range(3)]
        print("All work was submitted to the pool")

    pp([f.result() for f in futures])
    print("Done!")