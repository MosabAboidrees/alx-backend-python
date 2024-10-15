#!/usr/bin/env python3
"""
This module contains a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.
    Returns:
        float: The total runtime in seconds.
    """
    results = [i async for i in async_generator()]
    return results
