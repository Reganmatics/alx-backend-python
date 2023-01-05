#!/usr/bin/python3
"""
task 7. Complex types - strng and int/float to tuple
"""


def to_kv(k: str, v: int | float) -> tuple:
    """
    type-annoted function,
    args:
        k -> string
        v -> an int OR float

    return -> tuple
    """
    return (k, v**2)
