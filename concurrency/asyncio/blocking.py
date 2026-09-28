import asyncio
import datetime
import shutil
import tempfile
import urllib.request
from pprint import pp


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


async def coro_wrapper(url):
    # Allows to use the function in a loop
   return save_web_page_to_file(url)


async def main1():
    print("===== Blocking saved urls =====")
    tasks = []
    for _ in range(3):
        for url in urls:
            tasks.append(asyncio.create_task(coro_wrapper(url)))

    ft = await asyncio.gather(*tasks)
    print(f"Saved {len(ft)} urls:")
    pp(ft)

# The underlying sync function still blocks
started = datetime.datetime.now()
asyncio.run(main1())
finished = datetime.datetime.now()
print(f"Main1 done in {finished - started}")


async def main2():

    print("\n===== Blocking saved urls on worker threads =====")
    urls3 = urls * 3
    ft  = await asyncio.gather(*[
        asyncio.to_thread(save_web_page_to_file, x) for x in urls3
    ])
    print(f"Saved {len(ft)} urls:")
    pp(ft)

# Multiple threads for IO bound execution, the IO does not block
started = datetime.datetime.now()
asyncio.run(main2())
finished = datetime.datetime.now()
print(f"Main2 done in {finished - started}")
