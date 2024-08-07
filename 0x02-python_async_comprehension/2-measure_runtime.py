#!/usr/bin/env python3
"""Pyhton3.

Import async_comprehension from the previous file and
write a measure_runtime coroutine that will execute async_comprehension
four times in parallel using asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds,
-- this is because the single async_comprehension takes 10 sec
-- but the measure_runtime function is running all in parallel
-- so the overall time should be around 10 seconds
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel.

    using asyncio.gather.
    """
    start = time.perf_counter()
    running = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*running)
    end = time.perf_counter()
    return (end - start)
