#!/usr/bin/env python3
"""
Module for a function that returns the floor of a float number
with type annotations.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a float number.

    Args:
        n (float): The float number to floor.

    Returns:
        int: The floor of the float number n.
    """
    return math.floor(n)
