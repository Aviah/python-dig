# Typically asyncio Future is not very useful on its own
# It's mostly used by asyncio as the bridge between resources that are waited for, and the awaited coroutines execution
# Not thread safe
# Similar but not identical to concurrent.futures.Future

import asyncio
import time


async def do_something():
    print("Entered coroutine")
    await asyncio.sleep(1)
    print("Resume and exit coroutine")
    return 42

async def error_something():
    print("Entered error coroutine")
    await asyncio.sleep(1)
    return 10/0


def a_callback(f):
    print(f"\nCallback says:")
    print(f"The Future resolved: {f}")
    print(f"Result: {f.result()}")

def some_callback(f):
    print(f"\nCallback says:")
    time.sleep(0.11)
    f.set_result(42)
    print(f"The Future resolved: {f} to {f.result()}")
    print("Exit some_callback")

async def main():

    loop = asyncio.get_running_loop()
    t1 = loop.create_task(do_something())
    t2 = loop.create_task(error_something())
    f1 = loop.create_future()
    f1.add_done_callback(a_callback)

    print(f"Task created: {t1}")
    print(f"Task created: {t2}")
    print(f"Future created: {f1}")

    print("\nFutures?")
    print(f"t1: {asyncio.isfuture(t1)}")
    print(f"t2: {asyncio.isfuture(t2)}")
    print(f"f1: {asyncio.isfuture(f1)}")

    await asyncio.sleep(2)

    print("\nDone?")
    print(f"t1: {t1.done()}")
    print(f"t2: {t2.done()}")
    print(f"f1: {f1.done()}")

    print("\nSettings results for f1...")
    f1.set_result('spam')

    try:
        print("Settings results *again* for f1...")
        f1.set_result('foo')
    except Exception as e:
        print(repr(e))

    print("\nDone?")
    print(f"t1: {t1.done()}")
    print(f"t2: {t2.done()}")
    print(f"f1: {f1.done()}")


    print("\nExceptions:")
    print(f"t1: {t1.exception()}")
    print(f"t2: {t2.exception()}")
    print(f"f1: {f1.exception()}")

    print("\nResults:")
    print(f"t1: {t1.result()}")
    try:
        print(f"t2: {t2.result()}")
    except Exception as e:
        print(repr(e))  # Exception consumed, exit code will be 0
    print(f"f1: {f1.result()}")


    # Future is handy when you need to wait to a simple (not coroutine) function
    print("\n===== Waiting for a callback using a future =====")
    fc = loop.create_future()
    print("Schedule a callback on the loop...")
    h = loop.call_soon(some_callback, fc)
    print(f"Handle to the callback, not awaitable: {h}")
    await fc
    print("The loop executed the callback")




asyncio.run(main())