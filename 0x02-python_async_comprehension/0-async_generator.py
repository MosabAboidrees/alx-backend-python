#!/usr/bin/env python3
"""
This module contains an asynchronous generator function.

The `async_generator` function is a coroutine that loops 10 times,
each time asynchronously waiting for 1 second, and then yields a
random float number between 0 and 10.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops 10 times, each time asynchronously waits 1 second,
    then yields a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
