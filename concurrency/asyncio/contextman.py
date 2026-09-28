import asyncio
import uuid

from types import TracebackType


class DbConnection:


    def __init__(self):
        self.transaction_id = None
        self.should_fail = False

    async def begin_transaction(self):
        await asyncio.sleep(0.1)
        if self.transaction_id:
            raise RuntimeError
        self.transaction_id = str(uuid.uuid4())[:6]
        print (f"Connection says: Transaction started {self.transaction_id}")
        return self.transaction_id

    async def commit_transaction(self):
        await asyncio.sleep(0.1)
        if not self.transaction_id or self.should_fail:
            raise RuntimeError
        print (f"Connection says: Transaction commited {self.transaction_id}")
        self.transaction_id = None

    async def rollback_transaction(self):
        await asyncio.sleep(0.1)
        if not self.transaction_id:
            raise RuntimeError
        print (f"Connection says: Transaction rollback {self.transaction_id}")
        self.transaction_id = None

class TransactionMan:

    def __init__(self, conn):
        self._conn = conn

    async def __aenter__(self):
        tr = await self._conn.begin_transaction()
        print(f"Contextman says: Transaction started {tr}")

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        try:
            await self._conn.commit_transaction()
        except Exception:
            await self._conn.rollback_transaction()
            raise


async def execute_transaction(should_fail=False):

    conn = DbConnection()
    async with TransactionMan(conn):

        print(f"Running queries {conn.transaction_id}")
        await asyncio.sleep(0.5)
        print(f"Still running queries {conn.transaction_id}")
        if should_fail:
            conn.should_fail = True


async def main():

    print("===== Context manager simulation =====")
    t1 = asyncio.create_task(execute_transaction())
    t2 = asyncio.create_task(execute_transaction(should_fail=True))
    ft = await asyncio.gather(t1, t2, return_exceptions=True)
    print(ft)

    print("\n===== Asyncio's timeout context manager =====")
    try:
        print("Running a task with a timeout")
        async with asyncio.timeout(0.5):
            await asyncio.create_task(asyncio.sleep(1))
    except TimeoutError as e:
        print(repr(e))


asyncio.run(main())
