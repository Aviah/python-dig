import asyncio
import inspect
from pprint import pp


async def a_coro():

    print("Entered coro...")
    print(f"Current task name: {asyncio.current_task().get_name()}")
    await asyncio.sleep(0.1)




async def main():

    t1 = asyncio.create_task(a_coro(), name='t1')
    await t1
    print(f"\nTask name: {t1.get_name()}")
    print(f"Is done: {t1.done()}")
    print(f"Cancel requests for the task: {t1.cancelling()}")
    print(f"Canceled: {t1.cancelled()}")
    print(f"Wrapped coroutine: {t1.get_coro()}")
    print(f"Wrapped coroutine state: {inspect.getcoroutinestate(t1.get_coro())}")

    t2 = asyncio.create_task(a_coro(), name='t2')
    t3 = asyncio.create_task(a_coro(), name='t3')
    t4 = asyncio.create_task(a_coro(), name='t4')

    print("\nAll tasks on the loop:")
    # The event loop does *not* guarantee to keep a strong ref to a task: this is the developer responsibility
    pp(asyncio.all_tasks())
    loop = asyncio.get_event_loop()


asyncio.run(main())

