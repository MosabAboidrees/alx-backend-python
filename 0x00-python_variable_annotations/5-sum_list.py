#!/usr/bin/env python3
"""
Module for a function that sums a list of floats with type annotations.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floats and returns the result as a float.

    Args:
        input_list (List[float]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """
    return sum(input_list)
