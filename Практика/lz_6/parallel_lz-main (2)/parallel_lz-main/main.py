from potoki import no_threa, threa
from process import numbers
from asinxron import async_tasks, sync_tasks
import asyncio

async def main():

    first_1 = no_threa()
    first_2 = threa()
    second = numbers()
    third_1 = await async_tasks()
    third_2 = sync_tasks()
    
if __name__ == "__main__":
    asyncio.run(main()) 


