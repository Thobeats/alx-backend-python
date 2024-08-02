#!/usr/bin/env python3
"""Typed Functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function that sums a list of floats"""
    return lambda x: x * multiplier
