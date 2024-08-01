#!/usr/bin/env python3
"""Duck typing example module """
from typing import Union, Any, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """returns the first element from a sequence if it exists"""
    if lst:
        return lst[0]
    else:
        return None
