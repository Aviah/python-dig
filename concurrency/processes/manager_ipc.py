import datetime
import  multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor


def work(d,l):
    pid = mp.current_process().pid
    d[pid] = datetime.datetime.now().isoformat()
    l.append(pid)


if __name__ == '__main__':

    print(f"Main process PID: {mp.current_process().pid}")
    with mp.Manager() as m:
        print(f"Manager process PID: {m._process.pid}")
        d = m.dict()
        print(f"Shared dict {id(d)} is ready: {type(d)})")
        l = m.list()
        print(f"Shared list {id(l)} is ready: {type(l)})")

        with ProcessPoolExecutor(max_workers=5) as e:
            [e.submit(work, d, l) for _ in range(5)]

        print(d)
        print(l)


