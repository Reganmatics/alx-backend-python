#!/usr/bin/env python3
"""
The basic of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    asynchronous cprourine that waits for random delay bw 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
