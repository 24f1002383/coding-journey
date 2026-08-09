"""
This exercise stub and the test suite contain several enumerated constants.
Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it's memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).
You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if _contains(list_two, list_one):
        return SUBLIST
    if _contains(list_one, list_two):
        return SUPERLIST
    return UNEQUAL


def _contains(big, small):
    """Return True if `small` is a contiguous sub-sequence of `big`."""
    n, m = len(small), len(big)
    if n == 0:
        return True
    if n > m:
        return False
    for i in range(m - n + 1):
        if big[i:i + n] == small:
            return True
    return False