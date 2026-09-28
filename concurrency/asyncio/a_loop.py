import asyncio
import threading
import time


def loop_on_thread(loop):

    print(f"Enter thread: {threading.current_thread().name}")
    print(f"Starting loop: {loop}")
    loop.run_forever()


async def say_hello(msg=None):

    print(f"Hello from: loop {id(asyncio.get_running_loop())} on thread {threading.current_thread().name}")
    if msg:
        print(f"# This is the message: {msg}")
    return 42

l1 = asyncio.new_event_loop()
l2 = asyncio.new_event_loop()


t1 = threading.Thread(target=loop_on_thread, args=(l1,))
t1.start()
t2 = threading.Thread(target=loop_on_thread, args=(l2,))
t2.start()
print(f"Loop l1 {id(l1)} - {l1} is running: {l1.is_running()}")
print(f"Loop l2 {id(l2)} - {l2} is running: {l2.is_running()}")

print("===== Futures on loop on another thread =====")
f1 = asyncio.run_coroutine_threadsafe(say_hello(), l1)
f2 = asyncio.run_coroutine_threadsafe(say_hello(), l2)

# Note: this is a concurrent.futures.Future
# To await it in asyncio loop use:
# result = await asyncio.wrap_future(future)
print(f"f1 is {type(f1)}")
print(f"f2 is {type(f2)}")

print(f"f1 result: {f1.result()}")
print(f"f2 result: {f2.result()}")


async def cross_loop_coro(loop):

    me_run_on = asyncio.get_running_loop()
    other_loop = loop
    print(f"Running on loop {id(me_run_on)}, will run a coroutine on the other loop {id(other_loop)}")
    ft = asyncio.run_coroutine_threadsafe(
        say_hello(f"This was put on loop {id(other_loop)} by loop {id(me_run_on)}"),
        other_loop
    )
    wrapped = asyncio.wrap_future(ft)  # run coro threadsafe returns concurrent.futures.Future
    result = await wrapped
    return result

f3 = asyncio.run_coroutine_threadsafe(cross_loop_coro(l2), l1)
print(f"Cross-loop result: {f3.result()}")

print("\nStopping the loops...")
l1.call_soon_threadsafe(l1.stop)
l2.call_soon_threadsafe(l2.stop)
print(f"Loop l1 {id(l1)} - {l1} is running: {l1.is_running()}")
print(f"Loop l2 {id(l2)} - {l2} is running: {l2.is_running()}")
time.sleep(0.5)
print(f"Loop l1 {id(l1)} - {l1} is running: {l1.is_running()}")
print(f"Loop l2 {id(l2)} - {l2} is running: {l2.is_running()}")
