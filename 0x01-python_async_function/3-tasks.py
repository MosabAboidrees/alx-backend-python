#!/usr/bin/env python3

"""Module for task_wait_random function"""

import asyncio
from typing import Any

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that waits for a random delay.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The asyncio.Task object.
    """
    return asyncio.create_task(wait_random(max_delay))
