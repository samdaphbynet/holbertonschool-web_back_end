#!/usr/bin/python3
"""
    Import async_generator from the previous task and then write a coroutine
    called async_comprehension that takes no arguments.
    The coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        The line `return [value async for value in async_generator()]`
        is using an asynchronous comprehension to iterate over the values
        produced by the `async_generator` and return them as a list.
    """
    return [value async for value in async_generator()]
