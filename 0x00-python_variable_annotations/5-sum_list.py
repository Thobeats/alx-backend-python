#!/usr/bin/env python3
"""Typed Functions"""
from functools import reduce
from typing import List


def sum_list(input_list: List[float]) -> float:
    """A function that sums a list of floats"""
    return reduce(lambda agg, num: agg + num, input_list)
