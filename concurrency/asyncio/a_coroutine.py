# Coroutine is an object that can suspend and resume it's code execution

import asyncio
import gzip
import tempfile
import warnings


async def save_web_page_to_file():

    print("# Entered coroutine...")

    # For actual applications use external libs to read async html
    reader, writer = await asyncio.open_connection(
        "www.python.org", 443, ssl=True
    )

    print("# Resume after await: open connection")
    writer.write(
        b"GET / HTTP/1.0\r\n"
        b"Host: www.python.org\r\n"
        b"Accept: text/html\r\n"
        b"Accept-Encoding: identity\r\n"
        b"Connection: close\r\n"
        b"\r\n"
    )
    await writer.drain()
    print("# Resume after await: writer drain")

    response = await reader.read()
    print("# Resume after await: reader read")
    headers, _, body = response.partition(b"\r\n\r\n")
    if body.startswith(b"\x1f\x8b"):
        body = gzip.decompress(body)
    html = body.decode("utf-8")
    print(f"Got html page:\n {html[:200]}...\n")
    with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            delete=False,
            suffix=".html"
    ) as tmp_file:
        tmp_file.write(html)
        print(f"Saved www.python.org to {tmp_file.name}")

    writer.close()
    print("Coroutine done!")


if __name__ == '__main__':

    # The def async *function* is a kind of constructor of a coroutine *object*
    warnings.simplefilter("always", RuntimeWarning)  # prints identical warnings
    coro_object1 = save_web_page_to_file()  # never awaited
    print(f"Coro object 1 is: {coro_object1}")
    coro_object2 = save_web_page_to_file()  # never awaited
    print(f"Coro object 2 is: {coro_object2}")
    print(f"Is coroutine: {asyncio.iscoroutine(save_web_page_to_file)}")
    print(f"Is coroutine: {asyncio.iscoroutine(save_web_page_to_file())}")  # never awaited
    asyncio.run(save_web_page_to_file())