#!/usr/bin/env python3
"""asyncio basics module"""
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ takes max_delay and returns asyncio Task"""
    task = create_task(wait_random(max_delay))
    return task
