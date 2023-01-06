#!/usr/bin/env python3
"""
task 9. Let's duck type an iterable object
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    args:
        lst -> an interale sequance

    return -> a list of tuples of sequence, int
    """
    return [(i, len(i)) for i in lst]
