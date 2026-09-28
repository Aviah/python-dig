import asyncio
import datetime
import time


def callback_sleep(desc):
    loop = asyncio.get_running_loop()
    print(f"Entered callback... called by {desc}")
    print(f"Now: {datetime.datetime.now().isoformat()}")
    print(f"Monotonic time: {time.monotonic()}")
    print(f"Loop time: {loop.time()}")
    time.sleep(0.5)


async def coro_sleep(desc, animal):
    print(f"Entered coro... called by {desc}")
    print(f"I am the {animal}")

    loop = asyncio.get_running_loop()
    print(f"Now: {datetime.datetime.now().isoformat()}")
    print(f"Monotonic time: {time.monotonic()}")
    print(f"Loop time: {loop.time()}")
    await asyncio.sleep(1)
    print(f"Exit coro {animal}")


async def main():

    loop = asyncio.get_running_loop()

    loop.call_soon(callback_sleep, "call_soon")
    loop.call_later(3, callback_sleep, "call_later" )

    start_together = loop.time() + 3

    loop.call_at(start_together, loop.create_task, coro_sleep("call_at", "Beaver"))
    loop.call_at(start_together, loop.create_task, coro_sleep("call_at", "Capybara"))
    loop.call_at(start_together, loop.create_task, coro_sleep("call_at", "Eagle"))

    await asyncio.sleep(7)

    t = asyncio.create_task(asyncio.sleep(2))
    try:
        await asyncio.wait_for(t, timeout=1)
    except TimeoutError as e:
        print(repr(e))
        print(f"{t.get_name()} is canceled: {t.cancelled()}")


asyncio.run(main())
print("Done!")
print(f"Now: {datetime.datetime.now().isoformat()}")
print(f"Monotonic time: {time.monotonic()}")
