#!/usr/bin/env python3
"""
Task 1. Async Comprehensions
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[int]:
    """
    A coroutine that collects 10 random numbers using an async comprehension
    over async_generator,
    then returns the 10 random numbers.
    """
    async_gen = async_generator()
    random_nums = [num async for num in async_gen]
    return random_nums
