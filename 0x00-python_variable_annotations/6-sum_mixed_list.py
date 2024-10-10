#!/usr/bin/env python3
"""
Module for a function that sums a mixed list of integers and floats
with type annotations.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums a mixed list of integers and floats and returns the result as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The mixed list to sum.

    Returns:
        float: The sum of the list elements as a float.
    """
    return sum(mxd_lst)
