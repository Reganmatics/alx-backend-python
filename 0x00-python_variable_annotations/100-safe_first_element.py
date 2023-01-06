#!/usr/bin/env python3
"""
Advanced task
task 10. Duck typing - first element of a sequence
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    args:
        sequence
    return -> list OR NoneType
    """
    if lst:
        return lst[0]
    else:
        return None
