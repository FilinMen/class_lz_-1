import asyncio
import time

async def async_task(name, delay):

    await asyncio.sleep(delay)
    print(f"Задача {name} завершилась через {delay} секунд.")

async def async_tasks():
    
    work = [

        asyncio.create_task(async_task("A", 1)),
        asyncio.create_task(async_task("B", 2)),
        asyncio.create_task(async_task("C", 3)),
        asyncio.create_task(async_task("D", 4)),
        asyncio.create_task(async_task("E", 5))
    ]

    start = time.time()
    await asyncio.gather(*work)
    thread_time = time.time() - start
    print(f"Асинхронное выполнение заняло {thread_time:} секунд.")

def sync_tasks():

    start = time.time()
    for name, delay in [("A", 1), ("B", 2), ("C", 3), ("D", 4), ("E", 5)]:
        time.sleep(delay)
        print(f"Задача {name} завершилась через {delay} секунд.")
    thread_time = time.time() - start
    print(f"Последовательное выполнение заняло {thread_time:} секунд.")

