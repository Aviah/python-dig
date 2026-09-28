import asyncio

async def double_it(x):
    try:
        return x*2
    except Exception:
        await asyncio.sleep(0.1)
        raise


async def divide_it(x, y):
    try:
        return x / y
    except Exception:
        await asyncio.sleep(0.1)
        raise


async def find_id(d, k):
    try:
        return d[k]
    except Exception:
        await asyncio.sleep(0.1)
        raise

async def  sleep_5():
    await asyncio.sleep(5)


async def do_something():
    print("Doing something...")


async def add_task(tg):
    tg.create_task(do_something())


async def main():
    tasks = []
    try:
        async with asyncio.TaskGroup() as tg:
            tasks.append(tg.create_task(add_task(tg)))
            tasks.append(tg.create_task(sleep_5()))
            tasks.append(tg.create_task(double_it(2)))
            tasks.append(tg.create_task(double_it({1, 2})))
            tasks.append(tg.create_task(double_it({'1': 2})))
            tasks.append(tg.create_task(divide_it(1, 0)))
            tasks.append(tg.create_task(find_id({'foo': 'bar'}, 'spam')))

    # TaskGroup terminates on the first exception and then cancel all remaining tasks
    # So exception propagation from the coroutines was delayed to allow multiple exceptions
    except* TypeError as eg:
        print("Handling TypeError:")
        for exc in eg.exceptions:
            print(repr(exc))

    except* ZeroDivisionError as eg:
        print("Handling ZeroDivisionError:")
        for exc in eg.exceptions:
            print(repr(exc))

    except* Exception as eg:
        print("Handling all other exceptions:")
        for exc in eg.exceptions:
            print(repr(exc))

    finally:
        print("----- Finally clause -----")
        for t in tasks:
            try:
                m = t.result()
            except Exception:
                m = t.exception()
            except asyncio.CancelledError:
                m = "CancelledError"

            print(f"{t.get_name()}: canceled: {t.cancelled()}, result/exception: {m}")


asyncio.run(main())