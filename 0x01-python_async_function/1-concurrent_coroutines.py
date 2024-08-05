#!/usr/bin/env python3
"""Execute multiple coroutines at the same time with async."""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times with the specified max_delay."""
    running = [wait_random(max_delay) for _ in range(n)]
    delays = []
    for task in asyncio.as_completed((running)):
        delay = await task
        delays.append(delay)
    return delays
