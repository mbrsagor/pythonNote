import asyncio


async def say_hello():
    print('Hello there,')
    await asyncio.sleep(3)
    print(f'This is Sagor')


# asyncio.run(say_hello())


async def download():
    for i in range(0, 11):
        await asyncio.sleep(1)
        print(f"Download {i}% done")
    print("Thanks Sagor! Your download has been completed.")


asyncio.run(download())
