import asyncio
import urllib.request
import random
import tempfile
import shutil
from typing import Any


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

async def worker(name , tasks: asyncio.Queue[Any]):

    print(f"Worker started: {name}")
    while True:
        url =  await tasks.get()
        try:
            print(f"Worker {name}: picked a task. Remaining: {tasks.qsize()}")
            res = await asyncio.to_thread(save_web_page_to_file, url)
            print(f"Worker {name}: {res}")
        finally:
            tasks.task_done()

async def main():

    tasks = asyncio.Queue()
    workers = [asyncio.create_task(worker(name=f'W-{x}', tasks=tasks)) for x in range(3)]

    download = urls * 3
    random.shuffle(download)
    for url in download:
        await asyncio.sleep(0.05)
        await tasks.put(url)

    await tasks.join()
    print("Workers got all tasks")

    for w in workers:
        w.cancel()
    await asyncio.gather(*workers, return_exceptions=True)
    print("All workers canceled")


asyncio.run(main())




