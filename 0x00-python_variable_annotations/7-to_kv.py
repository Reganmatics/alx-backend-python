#!/usr/bin/env python3
"""
task 7. Complex types - strng and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    type-annoted function,
    args:
        k -> string
        v -> an int OR float

    return -> tuple
    """
    return (k, v**2)
