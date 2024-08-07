#!/usr/bin/env python3
"""Pyhton3.

0x02-python_async_comprehension
"""
import random
import asyncio
from typing import List


async def async_generator() -> float:
    """loop 10 times, each time asynchronously.

    wait 1 second, then yield a random number between 0 and 10.
    Use the random module.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
