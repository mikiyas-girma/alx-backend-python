#!/usr/bin/env python3
""" Module that measures the total execution time for async_comprehension
    called 4 times.
"""
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Method that measures the total execution time for async_comprehension
        called 4 times.
        Returns:
            float: the total execution time.
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
