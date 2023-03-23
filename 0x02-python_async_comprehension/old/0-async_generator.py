#!/usr/bin/env python3
"""
Task 0. Async Generator
"""
import asyncio
import random


async def async_generator() -> None:
    """
    args:
        None
    return -> Nontype
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
