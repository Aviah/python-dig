import inspect
import asyncio
import random

mammals = ("Dog", "Cat", "Bear", "Beaver", "Horse", "Whale")
birds = ("Eagle", "Falcon", "Albatross", "Pigeon", "Duck")
error = [lambda: 1 / 0]
async def ganimals(animals, times):

    try:
        while times:
            await asyncio.sleep(0.1)
            item = random.choice(animals)
            if callable(item):
                item = item()
            yield item
            times -= 1

    except Exception as e:
        print("Oops got an error, checking...")
        await asyncio.sleep(0.2)
        print("Disaster. I quit")
        raise

    finally:
        print("Clean up, takes some time")
        await asyncio.sleep(0.2)
        print("Ok, finished")


async def coro_print(g):
    async for a in g:
        print(a)


async def main():

    print("===== Async generator: async + yield")
    gmammals = ganimals(mammals, 5)
    print(inspect.isasyncgen(gmammals))  #
    animal = await anext(gmammals)
    print(animal)
    print(await gmammals.asend(None))
    await gmammals.aclose()


    print("\n===== Generator fully consumed =====")
    gmammals = ganimals(mammals, 5)
    gbirds = ganimals(birds, 3)

    t1 = asyncio.create_task(coro_print(gmammals))
    t2 = asyncio.create_task(coro_print(gbirds))
    await asyncio.gather(t1, t2)

    print("\n===== Generator raises exception =====")
    gerror = ganimals(error, 5)
    t3 = asyncio.create_task(coro_print(gerror))
    results = await asyncio.gather(t3, return_exceptions=True)
    print(results)



asyncio.run(main())


