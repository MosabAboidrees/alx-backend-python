#!/usr/bin/env python3
"""
This module contains asynchronous functions to measure the runtime of
executing multiple asynchronous comprehensions in parallel.

Functions:
    async_comprehension: Collects 10 random numbers using
    an async comprehension. measure_runtime: Measures the
    total runtime of executing async_comprehension
    four times in parallel.
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel using
    asyncio.gather and measure the total runtime."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
