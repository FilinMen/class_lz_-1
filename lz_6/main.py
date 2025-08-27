import asyncio
from event import event
from manager import manager
from period import main

if __name__ == "__main__":
    print("======")
    event()

    print("======")
    manager()

    print("======")
    asyncio.run(main())
