#!/usr/bin/env python3
"""
advanced task
More involved type annotations
"""
from typing import Any, Mapping, TypeVar, Union


K = TypeVar('K')
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, T], key: Any, default: None = None) -> \
        Union[Any, T]:
    """
    args:
        dct -> dictionary
        key -> dict key
        default -> None
    """
    if key in dct:
        return dct[key]
    else:
        return default
