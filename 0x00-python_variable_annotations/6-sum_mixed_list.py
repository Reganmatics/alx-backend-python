#!/usr/bin/env python3
"""
task 6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annoted function, sums up mxd_list
    args:
    mxd_list -> list of mixed data types of int and float

    return -> float
    """
    return sum(mxd_lst)
