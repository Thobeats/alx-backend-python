#!/usr/bin/env python3
"""Typed Functions"""
from functools import reduce
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """A function that sums a list of floats"""
    return [k, v*v]
