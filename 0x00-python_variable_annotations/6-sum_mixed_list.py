#!/usr/bin/env python3
"""
takes a list of integers and floats and returns their sum
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[float, int]])-> float:
    """return sum of mxd_lst"""
    return sum(mxd_lst)
