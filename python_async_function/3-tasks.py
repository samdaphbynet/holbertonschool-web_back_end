#!/usr/bin/env python3
"""
    function that takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        The line `return asyncio.create_task(wait_random(max_delay))`
        is creating a new asyncio task using the `create_task()` function.
        It is passing the `wait_random()` function with the `max_delay`
        argument as the coroutine to be executed by the task. The task is
        then returned by the function.
    """
    return asyncio.create_task(wait_random(max_delay))
