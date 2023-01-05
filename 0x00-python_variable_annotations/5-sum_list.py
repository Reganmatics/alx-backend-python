#!/usr/bin/env python3

"""
task 5: Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annoted function wihich takes a list of floats and returns a float
    args:
    input_list -> a list of floats

    return -> float
    """
    return sum(input_list)
