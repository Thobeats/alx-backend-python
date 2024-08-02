#!/usr/bin/env python3
"""Typed Functions"""
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """A function that sums a list of floats"""
    return reduce(lambda agg, num: agg + num, input_list)
