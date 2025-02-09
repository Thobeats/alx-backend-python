#!/usr/bin/env python3
"""Typed Functions"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Annotating the element length function"""
    return [(i, len(i)) for i in lst]
