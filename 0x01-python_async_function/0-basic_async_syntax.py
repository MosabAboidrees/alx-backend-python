"""
This module contains an asynchronous
coroutine that waits for a random delay.

    Waits for a random delay between 0 and max_delay seconds
     and returns the delay.

    Args:
    max_delay (int): The maximum delay in seconds. Default is 10.

    Returns:
    float: The actual delay in seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    # Define an asynchronous function that takes
    # an integer max_delay with a default value of 10
    # Generate a random float between 0 and max_delay
    delay = random.uniform(0, max_delay)
    # Pause the coroutine for the duration of the delay
    await asyncio.sleep(delay)
    # Return the actual delay
    return delay
