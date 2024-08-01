#!/usr/bin/env python3
""" Safely_get_value module docs"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar['T']
RET = Union[T, Any]
DEF = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: DEF = None) -> RET:
    """return a value using the key from a dict """
    if key in dct:
        return dct[key]
    else:
        return default
