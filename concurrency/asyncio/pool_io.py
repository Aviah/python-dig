import asyncio
import datetime
import urllib.request
import tempfile
import shutil
import concurrent.futures


urls = [
    'https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/',
    'https://www.joelonsoftware.com/2000/05/12/strategy-letter-i-ben-and-jerrys-vs-amazon/',
    'https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/',
    'https://www.joelonsoftware.com/2002/01/06/fire-and-motion/',
    'https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/',
]


def save_web_page_to_file(url):
    # Demo of a blocking function, for actual async use dedicated libraries
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            return f"Saved {url} to {tmp_file.name}"


POOL_MAX = 5

async def main():

    loop = asyncio.get_running_loop()

    print("===== Threadpool Executor =====")
    start = datetime.datetime.now()
    with concurrent.futures.ThreadPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, save_web_page_to_file, x) for x in urls * 3]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Threadpool finished after {datetime.datetime.now() - start}")


    print("\n===== Interpreter Pool Executor =====")
    print("Real multithreaded, interpreter per thread")
    start = datetime.datetime.now()
    with concurrent.futures.InterpreterPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, save_web_page_to_file, x) for x in urls * 3]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Interpreter pool, no GIL, finished after {datetime.datetime.now() - start}")

    print("\n===== Process Pool Executor =====")
    start = datetime.datetime.now()
    with concurrent.futures.ProcessPoolExecutor(max_workers=POOL_MAX) as pool:
        fts = [loop.run_in_executor(pool, save_web_page_to_file, x) for x in urls * 3]
        async for f in asyncio.as_completed(fts):
            print(f.result())
    print(f"Process pool finished after {datetime.datetime.now() - start}")

if __name__ == '__main__':
    asyncio.run(main())
