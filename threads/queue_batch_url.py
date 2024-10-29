import datetime
import queue
import threading
import urllib.request
import tempfile
import shutil

tasks = queue.Queue()
url_iterations = 10

urls = [
    'https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/',
    'https://www.joelonsoftware.com/2000/05/12/strategy-letter-i-ben-and-jerrys-vs-amazon/',
    'https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/',
    'https://www.joelonsoftware.com/2002/01/06/fire-and-motion/',
    'https://www.joelonsoftware.com/2002/02/13/the-iceberg-secret-revealed/',
]


def save_web_page_to_file(url):
    global saved_files_with_threads
    with urllib.request.urlopen(url) as response:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            shutil.copyfileobj(response, tmp_file)
            print(url)


def worker():
    global tasks
    while True:
        try:
            task = tasks.get(block=False)
        except queue.Empty:
            return
        save_web_page_to_file(task)
        tasks.task_done()


# Batch job, put everything beforehand
for url in urls:
    for _ in range(url_iterations):
        tasks.put(url)

# Run until all tasks are done, no task is added once the job starts
active_threads = []
started_on = datetime.datetime.now()
for url in urls:
    for _ in range(url_iterations):
        t = threading.Thread(target=worker)
        active_threads.append(t)
        t.start()

tasks.join()
duration = datetime.datetime.now() - started_on
print(f"Done with threads, took {duration.total_seconds()} seconds")  # Typically less than a second

print("=====")
started_on = datetime.datetime.now()
for url in urls:
    for _ in range(url_iterations):
        save_web_page_to_file(url)

duration = datetime.datetime.now() - started_on
print(f"Done without threads, took {duration.total_seconds()} seconds")  # Typically +14 seconds
