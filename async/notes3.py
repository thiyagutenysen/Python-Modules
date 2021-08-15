# async only works on python 3.7 and above versions
import asyncio


async def main():
    print('chella')
    await foo('billa')
    print('main code finished')


async def foo(text):
    await asyncio.sleep(5)
    print(text)

asyncio.run(main())
