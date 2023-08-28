#!/usr/bin/env python3
"""
     function with integers n and max_delay as arguments that measures the
     total execution time for wait_n(n, max_delay), and
     returns total_time / n. Your function should return a float.
"""
import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        The code is measuring the average time it takes to run a certain
        number of concurrent coroutines.
    """
    start_time = time.time()

    run(wait_n(n, max_delay))

    end_time = time.time()

    total_time = start_time - end_time

    average_time = total_time / n

    return average_time
