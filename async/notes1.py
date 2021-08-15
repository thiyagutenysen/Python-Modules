# async only works on python 3.7 and above versions
import asyncio

# synchronous programming means everything that i do runs sequentially
# asynchronous programming means that we don't wait for a single part of the code to finish before running other parts of the code
# This is very helpful when we are performing network operations when we wait for a response from the server

# Coroutines


async def main():
    print('chella')
# async keyword is used to wrap the function
# when we call this function, a coroutine object is returned
# to execute a coroutine function you need to used await to execute it
#
# main()     ---> this gives error, as vanilla python function calling won't work in coroutines
# to use await keyword it must be inside the asynchronous function
# await main() ---> this gives error too, bcz to call async function we need an event

asyncio.run(main())
# asyncio created an event loop, it added this function to it's event loop and then it ran

# Now how to use await keyword


async def foo(text):
    print(text)
    await asyncio.sleep(5)
    # asyncio.sleep returns me a couroutine function which is the sleep function
    # await function executes that sleep coroutine
    # await works here as it is inside a coroutine
