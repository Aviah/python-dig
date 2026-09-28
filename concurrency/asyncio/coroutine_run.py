import asyncio

async def do_something(x):
    print("Entered coroutine...")
    # When the loop is started with run(coro) it wraps the coro in a task
    task = asyncio.current_task()
    print(f"Wrapper Task: {task}")
    print(f"Task name: {task.get_name()}")
    print(f"I am the task's coroutine: {task.get_coro()}")
    print(f"On loop: {task.get_loop()}")

    await asyncio.sleep(x)
    print("Resumed after await: sleep")
    print(f"Coroutine done")



asyncio.run(do_something(1))
print("Done!")