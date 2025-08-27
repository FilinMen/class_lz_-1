import asyncio
import time

async def period():
    start_time = time.time()
    while time.time() - start_time < 20:
        print(f"Выполнено в {time.strftime('%X')}")
        await asyncio.sleep(2)  

async def main():
    await period()

asyncio.run(main())


