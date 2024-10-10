#!/usr/bin/env python3
"""
Module for a function that returns a tuple with a string
and the square of an int/float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string k and an int or float v, and returns a tuple
    with k and v squared as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): The value to square.

    Returns:
        Tuple[str, float]: A tuple containing k and the square of v as a float.
    """
    return (k, float(v ** 2))
