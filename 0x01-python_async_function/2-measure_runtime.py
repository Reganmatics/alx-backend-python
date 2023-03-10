#!/usr/bin/env python3
"""
Task 2. Measure the runtime
"""
import time
from typing import Tuple

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    args:
        n -> int
        max_delay -> int

    return -> float
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
