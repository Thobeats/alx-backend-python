#!/usr/bin/env python3
"""Typed Functions"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return the first element"""
    if lst:
        return lst[0]
    else:
        return None
