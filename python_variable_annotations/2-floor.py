#!/usr/bin/env python3
"""
    type-annotated function floor which takes a float n as
    argument and returns the floor of the float.
"""


def floor(n: float) -> int:

    """
        The code block `if n >= 0: return int(n)` checks if the
        input `n` is greater than or equal to 0.
        If it is, it returns the integer value of `n`
        using the `int()` function.
    """
    if n >= 0:
        return int(n)
    else:
        return int(n) - 1
