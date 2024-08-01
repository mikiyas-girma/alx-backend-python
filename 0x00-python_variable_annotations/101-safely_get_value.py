#!/usr/bin/env python3
""" Safely_get_value module docs"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """return a value using the key from a dict """
    if key in dct:
        return dct[key]
    else:
        return default
