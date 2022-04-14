

"""
Asynchronous means that you can execute multiple things at a time
and you don't have to finish executing the current thing
in order to move on to next one.
"""

import asyncio
import time


def sync_count(sleep_time):
    print(f"One with sleep time {sleep_time}")
    time.sleep(sleep_time)
    print(f"Two with sleep time {sleep_time}")


def sync_main():
    for num in [2, 1, 3]:
        sync_count(num)



async def async_count(sleep_time):
    print(f"One with sleep time {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"Two with sleep time {sleep_time}")



async def async_main():
    await asyncio.gather(async_count(2), async_count(1), async_count(3))


if __name__ == "__main__":
    
    start = time.time()


    # synchronous
    # sync_main()


    # async
    asyncio.run(async_main())


    end = time.time()
    elapsed = end - start

    print(f"{__file__} executed in {elapsed: .2f} seconds.")
