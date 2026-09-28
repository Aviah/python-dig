import asyncio


balance = 500

async def atm(tasks, balance_lock):
    global balance
    while True:
        req = await tasks.get()
        try:
            async with balance_lock:
                if balance < req:
                    print(f"Not enough balance! Balance is: {balance}")
                    continue
                print("Prrr... dispensing... ")
                await asyncio.sleep(0.1)
                balance -= req
                print(f"Withdrew {req}. Balance is: {balance}")
        finally:
            tasks.task_done()


async def notify_when_ready(event):
    print("Enter notifier...")
    await event.wait()
    print("Notifier says: Oi, it's ready!")


async def main():

    tasks = asyncio.Queue()
    balance_lock = asyncio.Lock()
    atms = [asyncio.create_task(atm(tasks, balance_lock)) for _ in range(3)]
    for _ in range(10):
        await  tasks.put(100)

    await tasks.join()
    for w in atms:
        w.cancel()
    await asyncio.gather(*atms, return_exceptions=True)

    ev = asyncio.Event()
    print("Creating notifier...")
    notifier = asyncio.create_task(notify_when_ready(ev))
    await  asyncio.sleep(0.1)
    print("Notifier created...")
    await asyncio.sleep(1)
    ev.set()
    await notifier


asyncio.run(main())