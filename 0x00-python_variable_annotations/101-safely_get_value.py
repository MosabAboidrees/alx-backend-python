#!/usr/bin/env python3
"""
Module for a function that safely gets a value from a mapping
with type annotations.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    Args:
        dct (Mapping): The dictionary to get the value from.
        key (Any): The key to search for.
        default (Union[T, None], optional): The default value to return
        if key is not found.
            Defaults to None.

    Returns:
        Union[Any, T]: The value associated with key if it exists,
        otherwise default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
