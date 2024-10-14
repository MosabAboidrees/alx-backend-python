#!/usr/bin/env python3
"""
This module provides a function `wait_n` that spawns a specified number of
coroutines using the `wait_random` function from the `0-basic_async_syntax`
module. The coroutines are executed concurrently, and the function returns
a list of delays in ascending order.

Functions:
    wait_n(n: int, max_delay: int) -> List[float]:
        Spawns `wait_random` n times with the specified max_delay
        and returns a list of all the delays in ascending order.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of all the delays in ascending order.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
