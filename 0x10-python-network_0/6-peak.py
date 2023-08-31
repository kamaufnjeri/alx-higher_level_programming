#!/usr/bin/python3
"""Module for peaking a peak season"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    lis = list_of_integers[:]
    if len(lis) == 0:
        return None
    if len(lis) == 1:
        return lis[0]
    if len(lis) == 2:
        if lis[1] > lis[0]:
            return lis[1]
        else:
            return lis[0]

    mid = len(lis) // 2
    middle = lis[mid]
    if middle > lis[mid - 1] and middle > lis[mid + 1]:
        return middle
    elif middle < lis[mid - 1]:
        return find_peak(lis[:mid])
    else:
        return find_peak(lis[mid + 1:])
