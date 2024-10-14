#!/usr/bin/env python3
"""
This module contains a function to measure the runtime
of an asynchronous function.

Functions:
    measure_time(n: int, max_delay: int) -> float:
        Measures the total execution time for wait_n(n, max_delay)
          and returns the average time per task.
    """

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average runtime of executing wait_n function.
    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay for each wait_n execution.
    Returns:
        float: The average runtime per execution of wait_n.
    """

    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
