#!/usr/bin/env python3
"""
Module for a function that safely returns the first element
of a sequence, with type annotations.
"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, else None.

    Args:
        lst (Sequence[Any]): The sequence to get the first element from.

    Returns:
        Union[Any, None]: The first element of lst if it exists, else None.
    """
    if lst:
        return lst[0]
    else:
        return None
