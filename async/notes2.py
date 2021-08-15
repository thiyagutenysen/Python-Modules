# async only works on python 3.7 and above versions
import asyncio


async def main():
    print('chella')
    await foo('billa')
    print('main code finished')
    # chella is printed
    # wait for 5 seconds
    # print billa
    # print main code finished
    # the above execution seems to be sequential
    # what if i dont want to wait till foo is executed and move forward to next line of code?
    # for this we need to use task - see next notes


async def foo(text):
    await asyncio.sleep(5)
    # the above line will make the function wait for 5 seconds
    print(text)
    # asyncio.sleep returns me a couroutine function which is the sleep function
    # await function executes that sleep coroutine
    # await works here as it is inside a coroutine

asyncio.run(main())
