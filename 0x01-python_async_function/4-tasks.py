#!/usr/bin/env python3
"""
Task 4. Tasks
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[asyncio.Task]:
    """
    args:
        n -> int
        max_delay -> int

    return -> typing.List
    """
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
