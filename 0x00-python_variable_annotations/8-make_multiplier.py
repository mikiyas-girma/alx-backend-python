#!/usr/bin/env python3
"""type-annotated function make_multiplier module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
     takes a float multiplier as argument and returns a
     function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
