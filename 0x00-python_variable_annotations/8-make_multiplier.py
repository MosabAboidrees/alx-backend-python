#!/usr/bin/env python3
"""
Module for a function that returns a function that multiplies
a float by a multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier to use.

    Returns:
        Callable[[float], float]: A function that multiplies
        a float by multiplier.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies a float by the stored multiplier.

        Args:
            x (float): The float number to multiply.

        Returns:
            float: The result of x multiplied by multiplier.
        """
        return x * multiplier

    return multiplier_function
