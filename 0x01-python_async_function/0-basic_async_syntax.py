#!/usr/bin/env python3
"""basic async syntax module"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits random delay and eventually returns"""
    wait_time = random.uniform(0, max_delay)
    asyncio.sleep(wait_time)
    return wait_time
