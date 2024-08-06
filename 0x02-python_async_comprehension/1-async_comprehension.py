#!/usr/bin/env python3
"""
async comprehension module
"""
from typing import List
from importlib import import_module


async_generator = import_module('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """uses list comprehension to return a list of 10 random numbers"""
    return [x async for x in async_generator()]
