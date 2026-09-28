# ===== This is the most important script to understand how asyncio works =====

# A Task is an object that:
#   - Is created on an event loop
#   - Wraps a coroutine
#   - Provides the mechanics to handle and suspend/resume many coroutines on the event loop
#   - Provides the mechanics for others to await for it's wrapped coroutine to finish, and get the coro returned value

"""
Using Tasks to suspend and resume coroutines on the asyncio event loop

* A Task is an object that wraps a coroutine.
* At any given moment, the loop waits for IO on multiple waiting sites (e.g. a file descriptors)
* These waiting sites were awaited for by coroutines that are wrapped by tasks.
* However, nobody has a mapping of these "waiting for IO sites" to a specific Task. It's all done using callbacks.
* If a resource is awaited, a callback for *this resource* had been registered beforehand
* When the resource is ready, e.g. a socket is ready and the OS selects it's FD, the loop schedules the callback
* This callback typically gets some data from the resource and resolves a Future (previously placed with an "await")
* The callback will also handle cleanup: e.g. the ready FD will not be watched by the loop further
* Once the callback resolved the Future, the Future schedules (another) callback: this one points to a specific task.
* The *Future's* callback job is to wake-up the Task and runs it's __step method
* Nor the loop neither the Task know or care what has returned from the await (e.g. a page read or a dns request or sleep).
* The only goal is to wake up a specific task and run it's __step, so it can resume the relevant coroutine
* The waked-up Task resums: Now it can and do resume it's own coroutinne
* The Task is "telling" it's coroutine: "look, something you (or coroutines you called) were awaiting for - just arrived"
* This "something" is the resolved Future that the coroutine (or one of the coroutines that it called) was waiting for
* The Tasks executres "coro.send(None)", the *coroutine* resumes (and it will also resume it's underlying coroutines if any)
* The relevant coroutine down the chain is now resumed.
* Note: In the script the Task resumes save_web_page_to_file, which awaits for more coros down the chain:
    >> save_web_page_to_file ... >> open_connection ... >> getaddrinfo
* So: A coroutine was waiting for a resource by placing "await", got a Future for it, suspended, and now resumes.
* The resumed coroutine has a handle to the Future. This is the same Fututre that is now resolved, and it's callback waked up the Task
* The resumed coroutine gets the result from the Future, and continue execution until the next await (which will yield back to the loop)
* Note: A resource may return with partial data, that is not enough to resume execution beyond the original await
    - E.g., note the "_wait_for_data" in the log
    - The socket might be ready with a chunk from the OS persepctive
    - The chunk may not be actually ready from the *coroutine's point of view*.
    - If this is the case, the coroutine will immidiatly suspend again and wait for more data
* Note: The flow is the same *regardless of the type of resource* that was awaited for
    - When an awaited resouce is ready, it's Future can be resolved
    - It may be via an external thread pool, external process pool, sleep, selected FD etc.
    - In all of these cases, the callbacks resume the correct task
    - Then the Task resumes it's coroutine, which will resume it's internal awaits chain
* Note: A Task IS a Future
    - This allows others to await for a Task.
    - A task has two main roles: (1) wake-up and resume a coroutine, and (2) allowing to await it and get the coroutine final value.
    - When a coroutine finishes, the task resolve *itself* with this value, and anything awaited for the Task can resume.
* Note: The implemntaion
    - When a Task is created: it's __step is immidiately scheduled on the loop
    - This is why a task must be created on a specific loop
    - When a Task is awaited: it yields *itself*, to provide the caller a handle for it *as a future*
    - If the Task is already complete, await for it will not suspend execution
"""


import gzip
import asyncio
import tempfile

async def save_web_page_to_file():

    # The real Task object uses: print(f"# Entered save web page from {asyncio.current_task().get_name()}")
    print(f"Entered save web page from {asyncio.tasks._py_current_task().get_name()}")

    # For actual applications use external libs to read async html
    reader, writer = await asyncio.open_connection(
        "www.python.org", 443, ssl=True
    )

    print("# Resumed *coroutine* after await: open connection")
    writer.write(
        b"GET / HTTP/1.0\r\n"
        b"Host: www.python.org\r\n"
        b"Accept: text/html\r\n"
        b"Accept-Encoding: identity\r\n"
        b"Connection: close\r\n"
        b"\r\n"
    )
    await writer.drain()
    print("# Resumed *coroutine* after await: writer drain")

    response = await reader.read()
    print("# Resumed *coroutine* after await: reader read")
    headers, _, body = response.partition(b"\r\n\r\n")
    if body.startswith(b"\x1f\x8b"):
        body = gzip.decompress(body)
    html = body.decode("utf-8")
    print(f"Got the html page:\n {html[:200]}...\n")
    with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
            suffix=".html"
    ) as tmp_file:
        tmp_file.write(html)
        print(f"Saved html from www.python.org to {tmp_file.name}")

    writer.close()
    print("# Coroutine save_web_page_to_file done!")


async def bloop():
    #The real Task object uses: print(f"# Entered bloop from {asyncio.current_task().name}")
    print(f"# Entered bloop from {asyncio.tasks._py_current_task().get_name()}")
    for i in range(3):
        await asyncio.sleep(0.05)
        print(f"Resumed *coroutine* after await: bloop {i}")

async def main():
    # The real Task object uses: print(f"Entered main from {asyncio.current_task().get_name()}")
    print(f"# Entered main from {asyncio.tasks._py_current_task().get_name()}")

    task_bloop1 = asyncio.create_task(bloop(), name='Task-bloop-1')
    task_web1 = asyncio.create_task(save_web_page_to_file(), name="Task-save-page-1")
    await  asyncio.gather(task_bloop1, task_web1)
    print("Main done!")



class TaskWithStepLogger(asyncio.tasks._PyTask):
    """
    Factory for demo only
    _PyTask keeps ref the Python implementation and not the CPython
    """

    def _Task__step(self, *args, **kwargs):

        print(f">> Resume execution of *task*: {self.get_name()}")
        super()._Task__step(*args, **kwargs)


    def _Task__wakeup(self, future):
        import inspect

        coro = self.get_coro()
        chain = []

        while inspect.iscoroutine(coro):
            frame = coro.cr_frame

            chain.append(
                f"{coro.cr_code.co_name}"
                f":{frame.f_lineno if frame else '?'}"
            )

            coro = coro.cr_await

        print(
            f"<< Wakeup: {self.get_name()}\n"
            f"   Future: {future!r}\n"
            f"   Await chain: {' -> '.join(chain)}"
        )

        return super()._Task__wakeup(future)

def task_factory(loop, coro, **kwargs):
    return TaskWithStepLogger(coro, loop=loop, **kwargs)


loop = asyncio.new_event_loop()
loop.set_task_factory(task_factory)
loop.run_until_complete(main())


