#!/usr/bin/env python3
"""Typed Functions"""
from typing import Mapping, Any, TypeVar, Union
T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """get the value if it exists"""
    if key in dct:
        return dct[key]
    else:
        return default
