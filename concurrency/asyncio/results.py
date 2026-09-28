import asyncio
import time


def pow_callback(x, y, ft):
    time.sleep(0.5)
    ft.set_result(pow(x, y))

async def repeat_coro(animal, n):
    await asyncio.sleep(0.5)
    fixed = animal.capitalize()
    return fixed * n

async def main():
    t1 = asyncio.create_task(repeat_coro("buffalo", 8))
    while True:
        if not t1.done():
            print('Not ready yet...')
            await asyncio.sleep(0.1)
            continue
        print(f"The result of the coro is: {t1.result()}")
        break

    loop = asyncio.get_running_loop()
    f1 = loop.create_future()
    loop.call_soon(pow_callback, 2, 16, f1)
    result = await f1  # await retrieves the result of an awaitable (or propagates its exception)
    print(f"The result of the callback is: {result}")


asyncio.run(main())
