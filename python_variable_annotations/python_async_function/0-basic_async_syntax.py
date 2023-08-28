#!/usr/bin/env python3
"""
    asynchronous coroutine that takes in an integer argument (max_delay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds and
    eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        The code `delay = max_delay * random.random()` generates a random
        delay between 0 and`max_delay` (inclusive) by multiplying `max_delay`
        with a random float value between 0 and 1.
    """
    delay = max_delay * random.random()
    await asyncio.sleep(delay)
    return delay
