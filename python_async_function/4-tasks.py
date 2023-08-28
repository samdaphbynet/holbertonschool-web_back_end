#!/usr/bin/env python3
"""
    Import task_wait_random from the "0-basic_async_syntax.py" and
    write an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay. You will spawn task_wait_random n times with
    the specified max_delay.
    wait_n should return the list of all the delays (float values). The list of
    the delays should be in ascending order without using sort() because of
    concurrency.
"""
import asyncio
import random
from typing import List, Optional


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        The function creates multiple tasks that each wait for a
        random delay and returns a list of the
        delays.
        :return: The code is returning a list of delays.
    """
    async def wrapper():
        """
            :return: The code is returning a list of delays.
        """
        return await task_wait_random(max_delay)

    delays = []
    tasks = [wrapper() for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
