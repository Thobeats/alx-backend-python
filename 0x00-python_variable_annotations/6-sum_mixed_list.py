#!/usr/bin/env python3
"""Typed Functions"""
from functools import reduce
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A function that sums a list of floats"""
    return reduce(lambda agg, num: agg + num, mxd_lst)
