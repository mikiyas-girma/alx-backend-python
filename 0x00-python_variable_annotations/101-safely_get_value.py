#!/usr/bin/env python3
""" Safely_get_value module docs"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar['T']
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """return a value using the key from a dict """
    if key in dct:
        return dct[key]
    else:
        return default
