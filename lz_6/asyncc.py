import asyncio
class Asynchron:

    def __init__(self):
        self.delay = 3

    async def task_error(self):

        await asyncio.sleep(self.delay)
        raise ValueError("Не работает!")

    async def handler(self):

        print("Запущенно")

        try:
            result = await self.task_error()
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка")

        print("Завершено")



if __name__ == "__main__":
    process = Asynchron()
    asyncio.run(process.handler())
