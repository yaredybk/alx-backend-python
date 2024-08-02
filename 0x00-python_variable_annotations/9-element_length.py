#!/usr/bin/env python3
"""Annotations example module """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ returns the length of list of sequences """
    return [(i, len(i)) for i in lst]
