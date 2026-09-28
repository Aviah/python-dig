import asyncio

async def double_it(v):
    print(f"Doubling {v}")
    await asyncio.sleep(0.2)
    if v == 1000 or v==1001:
        await asyncio.sleep(2)
    return v * 2


async def main():

    print("===== asyncio.wait =====")
    tasks = []
    for s in ([1,2], "spam", "foo", "bar"):
        tasks.append(asyncio.create_task(double_it(s)))
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    for t in done:
        print(t.result())

    print("\n-----")
    tasks = []
    for s in ([1,2], "spam", "foo", {"a": 1}, 100, {1, 2, 3}, 1000, 1001):
        tasks.append(asyncio.create_task(double_it(s)))

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)  # also FIRST_COMPLETED, ALL_COMPLETED
    for t in done:
        try:
            print(t.result())
        except Exception as e:
            print(t.exception())

    print("----- Pending -----")
    # when asyncio.wait finishes it does not cancel remaining tasks
    for t in pending:
        print(t)
        t.cancel()
    await asyncio.gather(*pending, return_exceptions=True)

    print("\n===== Gather =====")
    tasks = []
    for s in ([1,2], "spam", "foo", {"a": 1}, 100, {1, 2, 3}, 100, 1001):
        tasks.append(asyncio.create_task(double_it(s)))

    results = await asyncio.gather(*tasks, return_exceptions=True)
    print("----- Gather results:-----")
    print(results)


    print("\n===== As completed =====")
    tasks = []
    for s in (1000, 1001, [1, 2], "spam", "foo", {"a": 1}, 100, {1, 2, 3}):
        tasks.append(asyncio.create_task(double_it(s)))

    async for t in asyncio.as_completed(tasks):
        try:
            print(t.result())
        except Exception as e:
            print(t.exception())


    # TaskGroup: see tg.py

asyncio.run(main())





