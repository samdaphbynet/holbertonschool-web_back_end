#!/usr/bin/env python3
"""
    Import wait_random from the "0-basic_async_syntax.py" and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn wait_random n times with
    the specified max_delay.
    wait_n should return the list of all the delays (float values). The list of
    the delays should be in ascending order without using sort() because of
    concurrency.
"""
import asyncio
import random
from typing import List, Optional


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    async def wrapper():
        """
            The above function creates multiple tasks that each wait
            for a random delay, and then returns a
            list of the delays.
            :return: The code is returning a list of delays.
        """
        return await wait_random(max_delay)

    delays = []
    tasks = [wrapper() for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
