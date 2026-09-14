import datetime
import time
from concurrent.futures import ProcessPoolExecutor, wait


def work():
    for i in range(10):
        time.sleep(0.05)
    return i


def sleep_for(sec):
    time.sleep(sec)

def div_by_zero():
    return 1/0


if __name__ == '__main__':

    print("===== Future introspection =====")
    with ProcessPoolExecutor(max_workers=1) as ppe:

        f = ppe.submit(work)
        f.add_done_callback(lambda x: print(f"{x}: Callback done"))

        print(f"Future running: {f.running()}")
        print(f"Future done: {f.done()}")

    print("Pool finished")
    print(f"Future running: {f.running()}")
    print(f"Future done: {f.done()}")
    print(f"Future result: {f.result()}")


    print("\n===== Cancel after starting =====")
    with ProcessPoolExecutor(max_workers=1) as ppe:

        f = ppe.submit(work)
        f.add_done_callback(lambda x: print(f"{x}: Callback done"))
        print("Canceling future after it's started...")
        f.cancel()
        print(f"Future canceled: {f.cancelled()}")

    print("Pool finished")
    print(f"Future running: {f.running()}")
    print(f"Future done: {f.done()}")
    print(f"Future result: {f.result()}")

    print("\n===== Cancel before starting =====")
    with ProcessPoolExecutor(max_workers=1) as ppe:

        ppe.submit(work)
        f = ppe.submit(work)
        f.add_done_callback(lambda x: print(f"{x}: Callback done"))
        print("Canceling future before it's started...")
        f.cancel()
        print(f"Future canceled: {f.cancelled()}")

    print("Pool finished")
    print(f"Future running: {f.running()}")
    try:
        print(f"Future result: {f.result()}")
    except Exception as e:
        print(f"Asking for result from a canceled future: {repr(e)}")
    print(f"Future done: {f.done()}")


    print("\n===== Future exception =====")
    with ProcessPoolExecutor(max_workers=1) as ppe:

        print("Submitting a task that excepts")
        f = ppe.submit(div_by_zero)
        f.add_done_callback(lambda x: print(f"{x}: Callback done"))

        print(f"Future running: {f.running()}")
        print(f"Future done: {f.done()}")

    print("Pool finished")
    print(f"Future running: {f.running()}")
    print(f"Future done: {f.done()}")
    try:
        print(f"Future result: {f.result()}")
    except Exception as e:
        print(repr(e))

    print("\n===== Waiting for some of the futures =====")

    with ProcessPoolExecutor(max_workers=3) as ppe:

        fast_futures = [ppe.submit(sleep_for, 0.5) for _ in range(5)]
        slow_futures = [ppe.submit(sleep_for, 1) for _ in range(5)]

        wait(fast_futures)
        print(f"Fast futures finished: {datetime.datetime.now().isoformat()}")
    print(f"All futures finished: {datetime.datetime.now().isoformat()}")



