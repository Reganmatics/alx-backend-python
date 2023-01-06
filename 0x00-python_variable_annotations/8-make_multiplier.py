#!/usr/bin/env python3
"""
task 8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annoted function -> decorator function
    args:
        multiplier -> float

    return -> multiply
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
