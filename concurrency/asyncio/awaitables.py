# The core awaitables are Coroutines, Futures and Tasks.
# Task IS a future, and a wrapper of a coroutine (see a_task.py)
# The coroutine __await__ will drive the coroutine forward with send, throw and next, until it suspend and yields
# The future __await__ yields itself and suspends if it's not done. If done, it returns its result (or exception)
# Asyncio awaitable constructs return a coroutine or a future or a task


import asyncio


async def coro():
    await asyncio.sleep(0.1)
    print("coro done!")


async def coro_resolve_future(ft):
    await asyncio.sleep(0.1)
    ft.set_result(42)
    print("coro_resolve_future done!")


async def coro_set_event(ev):
    await asyncio.sleep(0.1)
    ev.set()
    print("coro_set_event done!")


async def main():

    loop = asyncio.get_running_loop()

    await coro()  # coroutine
    aw = loop.create_future()
    asyncio.create_task(coro_resolve_future(aw))
    await aw  # future

    aw = asyncio.create_task(coro())
    await aw  # task

    aw1 = asyncio.create_task(coro())
    aw2 = asyncio.create_task(coro())
    aw3 = asyncio.gather(aw1, aw2)
    await aw3  # future

    ev = asyncio.Event()
    asyncio.create_task(coro_set_event(ev))
    await ev.wait()  # coroutine

    tasks = asyncio.Queue()
    await tasks.put(42)  # coroutine
    await tasks.get()  # coroutine
    tasks.task_done()
    await tasks.join()  # coroutine

    aw1 = loop.create_future()
    aw2 = asyncio.create_task(coro_resolve_future(aw1))
    aw3 = coro()
    await asyncio.gather(aw1, aw2, aw3)


asyncio.run(main())