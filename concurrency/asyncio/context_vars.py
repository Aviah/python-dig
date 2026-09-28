# asyncio keeps the context var per the task scope

import asyncio

from contextvars import ContextVar


ctxv = ContextVar('ctxv', default = "spam")

async def coro_nested():
    print(f"Nested says: {ctxv.get()}")
    ctxv.set(2 * ctxv.get())

async def coro_parent(context_val):
    print(f"Parent says: {ctxv.get()}")
    await asyncio.sleep(0.1)
    print(f"Setting value...")
    ctxv.set(context_val)
    print(f"Parent changed to: {ctxv.get()}")
    await coro_nested()
    print(f"Parent says again: {ctxv.get()}")


async def main():

    print(f"Initial value: {ctxv.get()}")
    t1 = asyncio.create_task(coro_parent("bloop"))
    t2 = asyncio.create_task(coro_parent("jump"))
    await asyncio.gather(t1, t2)
    print(f"Final value: {ctxv.get()}")

asyncio.run(main())

