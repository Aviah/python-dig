import asyncio


async def inner():

    try:
        print("Enter Inner")
        await asyncio.sleep(0.3)
        print("Exit Inner")
    except asyncio.CancelledError:
        print("Inner canceled")
        raise


async def outer():
    try:
        print("Enter Outer")
        inner_task = asyncio.create_task(inner())
        print("Outer starting await for inner task...")
        await inner_task
        print("Exit Outer")
    except asyncio.CancelledError:
        print("Outer canceled")
        raise

async def outer_shields_inner():
    try:
        print("Enter Outer")
        inner_task = asyncio.create_task(inner())
        ft = asyncio.shield(inner_task)
        print(f"Shield: {ft}")
        print("Outer start await for the shield future of the inner task...")
        await ft
        print("Exit Outer")
    except asyncio.CancelledError:
        print("Outer canceled")
        raise


async def main():

    print("\n===== Nested tasks =====")
    t1 = asyncio.create_task(outer())
    await t1

    print("\n===== Nested tasks, cancel outer =====")
    t2 = asyncio.create_task(outer())
    await asyncio.sleep(0.05)
    t2.cancel()
    await asyncio.gather(t2, return_exceptions=True)

    print("\n===== Nested tasks, cancel outer, shield inner =====")
    t3 = asyncio.create_task(outer_shields_inner())
    await asyncio.sleep(0.05)
    t3.cancel()
    await asyncio.gather(t3, return_exceptions=True)

    # Let the inner task complete before main exits and cancel it
    await asyncio.sleep(0.5)

asyncio.run(main())