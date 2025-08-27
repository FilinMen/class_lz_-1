import asyncio

async def fail():
    await asyncio.sleep(3)
    raise ValueError("Вы явно что-то попутали,тут ничего работать не будет🙈")  

async def main():
    try:
        await fail()
    except ValueError as e:
        print(f"Исключение обработано: {e}")

asyncio.run(main())
