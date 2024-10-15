#!/usr/bin/env python3
"""
This module contains a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""

import asyncio
import time
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """
    Measure the total runtime of executing
    async_comprehension four times in parallel.
    Returns:
        float: The total runtime in seconds.
    """
    results = [i async for i in async_generator()]
    return results
