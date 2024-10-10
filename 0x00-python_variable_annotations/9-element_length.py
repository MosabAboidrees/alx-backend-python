#!/usr/bin/env python3
"""
Module for a function that returns element lengths with type annotations.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples
    containing each sequence and its length.

    Args:
        lst (Iterable[Sequence]): The iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple
        contains a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
