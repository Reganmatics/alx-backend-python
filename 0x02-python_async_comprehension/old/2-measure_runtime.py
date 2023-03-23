#!/usr/bin/env python3
"""
Task 2. Runtiem for four parallel comprehensions
"""
import asyncio
from datetime import datetime
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    args: None
    return -> float
    """
    start = datetime.now()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = datetime.now()
    total = (end - start).total_seconds()

    return total
