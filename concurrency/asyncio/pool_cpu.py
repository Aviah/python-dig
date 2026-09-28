import asyncio
import datetime
import concurrent.futures


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

POOL_MAX = 5
async def main():

    loop = asyncio.get_running_loop()

    print("===== Threadpool Executor =====")
    start = datetime.datetime.now()
    with concurrent.futures.ThreadPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, fib, 35) for _ in range(10)]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Threadpool finished after {datetime.datetime.now() - start}")


    print("\n===== Interpreter Pool Executor =====")
    print("Real multithreaded, interpreter per thread")
    start = datetime.datetime.now()
    with concurrent.futures.InterpreterPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, fib, 35) for _ in range(10)]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Interpreter pool, no GIL, finished after {datetime.datetime.now() - start}")

    print("\n===== Process Pool Executor =====")
    start = datetime.datetime.now()
    with concurrent.futures.ProcessPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, fib, 35) for _ in range(10)]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Process pool finished after {datetime.datetime.now() - start}")

if __name__ == '__main__':
    asyncio.run(main())
