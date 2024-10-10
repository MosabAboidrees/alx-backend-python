#!/usr/bin/env python3
"""
Module for a function that zooms an array with type annotations.
"""

from typing import List, Tuple, Any, Union, Sequence


def zoom_array(lst: Sequence[Any], factor: Union[int, float] = 2) -> List[Any]:
    """
    Zooms in an array by repeating its items by a given factor.

    Args:
        lst (Sequence[Any]): The input array to zoom.
        factor (Union[int, float], optional): The zoom factor. Defaults to 2.

    Returns:
        List[Any]: The zoomed array as a list.
    """
    zoomed_in: List[Any] = [
        item for _ in range(int(factor))
        for item in lst
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
