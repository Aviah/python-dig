import asyncio
import random

mammals = ("Dog", "Cat", "Bear", "Beaver", "Horse", "Whale")
birds = ("Eagle", "Falcon", "Albatross", "Pigeon", "Duck")


class AnimalIterator:

    def __init__(self, source, times):
        self._source = source
        self._sleep = random.choice((0.03, 0.1))
        self._times = times
        self._count = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._count >= self._times:
            raise StopAsyncIteration  # https://peps.python.org/pep-0492/#why-stopasynciteration

        await asyncio.sleep(self._sleep)
        self._count += 1
        return random.choice(self._source)


async def animals(source, times):
    async for a in AnimalIterator(source, times):
        print(a)


async def main():

    t1 = asyncio.create_task(animals(mammals, 5))
    t2 = asyncio.create_task(animals(birds, 3))
    await asyncio.gather(t1, t2)
    # Note: For async comprehensions see https://peps.python.org/pep-0530/#await-in-comprehensions


asyncio.run(main())