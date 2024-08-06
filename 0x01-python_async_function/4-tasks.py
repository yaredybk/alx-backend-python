#!/usr/bin/env python3
"""task_wait_random.

Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""


import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, task_max_delay: int) -> List[float]:
    """Spawn wait_random n times."""
    delays: List[float] = []

    running = [task_wait_random(task_max_delay) for _ in range(n)]

    for task in asyncio.as_completed((running)):
        delay = await task
        delays.append(delay)

    return delays
