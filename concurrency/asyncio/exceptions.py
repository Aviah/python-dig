# Exception that was retrieved will not propagate
# await retrieves the exception and propagate it

import asyncio
import sys


def error_callback():
    print("Entered error callback...")
    return {'foo':'bar'}['spam']


def add_100_callback(x, ft):
    print("Entered add_100_callback...")
    try:
        ft.set_result(x + 100)
    except Exception as e:
        ft.set_exception(e)


async def error_coro():
    print("Entered error coroutine...")
    return 10/0


# Exception handler (will work for callbacks)
def exp_handler(loop, context):

    msg = context['message']
    ex = context['exception']
    task = context.get('task')
    ft = context.get('future')
    handle = context.get('handle')

    print("Enter exception handler...")
    print(f"Asyncio message: {msg}")
    print(f"The exception: {repr(ex)}")
    if task:
        print(f"Task: {task}")

    if ft:
        print(f"Future: {ft}")

    if handle:
        print(f"Handle: {handle}")

    print("Handler ignores the exception, continue...")


async def main1():

    print("===== Retrieve exception with await =====")
    t1 = asyncio.create_task(error_coro())
    try:
        await t1  # will not work for callbacks
    except Exception as e:
        print(repr(e))

asyncio.run(main1())


async def main2():

    print("===== Retrieve exceptions with exceptions handler =====")
    t1 = asyncio.create_task(error_coro())
    try:
        await t1  # will not work for callbacks
    except Exception as e:
        print("The await got the exception, so the loop handler does not see it")
        print(repr(e))
        print("Main ignores the exception, continue...")

    asyncio.get_running_loop().call_soon(error_callback)

    asyncio.create_task(error_coro())
    await asyncio.sleep(1)  # Nobody retrieve the exception, will go to the handler

loop_e = asyncio.new_event_loop()
loop_e.set_exception_handler(exp_handler)
loop_e.run_until_complete(main2())

async def main3():

    print("===== Retrieve exceptions with other constructs =====")
    t1 = asyncio.create_task(error_coro())
    t2 = asyncio.create_task(error_coro())
    ft = asyncio.gather(t1, t2, return_exceptions=True)
    await ft
    print("Gather retrieved the exception as a result:")
    print(ft.result())

    t3 = asyncio.create_task(error_coro())
    t4 = asyncio.create_task(error_coro())
    done, _ = await  asyncio.wait((t3, t4))
    print("Wait retrieved the exceptions:")
    for d in done:
        print(d.exception())  # retrieve the exceptions

    import traceback
    print("The actual exceptions:")
    traceback.print_exception(ft.result()[0], file=sys.stdout)
    traceback.print_exception(done.pop().exception(),file=sys.stdout)

asyncio.run(main3())



async def main4():

    print("===== Callback sets exception of the Future =====")
    loop = asyncio.get_running_loop()
    f1 = loop.create_future()
    loop.call_soon(add_100_callback, "foo", f1)
    await asyncio.sleep(1)
    if not f1.exception():
        print(f1.result())
    else:
        print(f1.exception())

# except*: see tg.py
asyncio.run(main4())
