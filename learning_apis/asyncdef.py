import asyncio

async def my_task():
    print('Task started')
    await asyncio.sleep(1)
    print('Task completed')

asyncio.run(my_task())