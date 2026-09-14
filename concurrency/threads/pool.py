
import concurrent
from concurrent.futures.thread import ThreadPoolExecutor
import datetime
import queue
import shutil
import tempfile
import urllib.request

tasks = queue.Queue()
url_iterations = 3

urls = [
    'https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/',
    'https://www.joelonsoftware.com/2000/05/12/strategy-letter-i-ben-and-jerrys-vs-amazon/',
    'https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/',
    'https://www.joelonsoftware.com/2002/01/06/fire-and-motion/',
    'https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/',
]


def save_web_page_to_file(url):
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            result = (f"Saved {url} to {tmp_file.name}")
    return result

for mw in (3,15):
    tpe = ThreadPoolExecutor(max_workers=mw)
    futures = []
    started_on = datetime.datetime.now()
    for url in urls:
        for _ in range(url_iterations):
            f = tpe.submit(save_web_page_to_file, url)
            futures.append(f)
    for f in concurrent.futures.as_completed(futures):
        print(f.result())
    tpe_duration = datetime.datetime.now() - started_on
    print(f"Done with pool of {mw} max workers after {tpe_duration}")
