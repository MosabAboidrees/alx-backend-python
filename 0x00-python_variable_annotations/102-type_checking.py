#!/usr/bin/env python3
"""
Module for a function that zooms an array with type annotations.
"""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List[Any]:
    """
    Zooms in an array by repeating its items by a given factor.

    Args:
        lst: The input array to zoom.
        factor: The zoom factor. Defaults to 2.

    Returns:
        List: The zoomed array as a list.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
