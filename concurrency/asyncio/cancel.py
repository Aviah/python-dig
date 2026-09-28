import asyncio
import inspect


async def sleep_1_sec():
    await  asyncio.sleep(1)
    print("Slept 1 second")

async def something():
    try:
        print("Slept 1 second")
        await  asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Me canceled")
        raise

async def sleep_3_secs():
    await asyncio.sleep(3)
    print("Slept 5 seconds")

async def hog(n):

    async def fib(m):
        await asyncio.sleep(0.01)
        if m <= 1:
            return m
        else:
            result = await fib(m - 1) + await fib(m - 2)
            print(f"Fibonacci for {m} is {result}")
            return result
    try:
        return await fib(n)
    except asyncio.CancelledError:
        print("\nOops, I was canceled")  # The coroutine got the cancel request
        await  asyncio.sleep(1)
        # Python docs recommend to avoid uncanceling by the end user
        raise

async def main():

    loop = asyncio.get_running_loop()

    t1 = loop.create_task(sleep_1_sec())
    t2 = loop.create_task(hog(10))

    await asyncio.sleep(1.5)
    t3 = loop.create_task(sleep_3_secs())


    print("\n===== Cancel request =====")
    print(f"t1 cancel: {t1.cancel()}, done: {t1.done()}, state: {inspect.getcoroutinestate(t1.get_coro())}")
    print(f"t2 cancel: {t2.cancel()}, done: {t2.done()}, state: {inspect.getcoroutinestate(t2.get_coro())}")
    print(f"t3 cancel: {t3.cancel()}, done: {t3.done()}, state: {inspect.getcoroutinestate(t3.get_coro())}")

    try:
        await t3
    except asyncio.CancelledError:
        print("Oops, t3 was canceled")  # awaiting a canceled task

    print("\n===== Canceling? =====")
    print(f"t1 cancel requests: {t1.cancelling()}, done: {t1.done()}, state: {inspect.getcoroutinestate(t1.get_coro())}")
    print(f"t2 cancel requests: {t2.cancelling()}, done: {t2.done()}, state: {inspect.getcoroutinestate(t2.get_coro())}")
    print(f"t3 cancel requests: {t3.cancelling()}, done: {t3.done()}, state: {inspect.getcoroutinestate(t3.get_coro())}")

    await asyncio.wait((t2,))  # t2 delays the cancellation
    print("\n===== Canceled? =====")
    print(f"t1 canceled: {t1.cancelled()}")
    print(f"t2 canceled: {t2.cancelled()}")
    print(f"t3 canceled: {t3.cancelled()}")


    print("\n===== Await cancellation with gather =====")
    tasks = [asyncio.create_task(something()) for _ in range(3)]
    await asyncio.sleep(0.1)
    for t in tasks:
        t.cancel()
    ft = await asyncio.gather(*tasks, return_exceptions=True)
    print(ft)
    print("All canceled")


asyncio.run(main())
print("\nDone!")
