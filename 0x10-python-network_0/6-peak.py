#!/usr/bin/python3
"""A fuction to fine peak"""


def find_peak(list_of_integers):
    """The function"""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    middle = list_of_integers[mid]
    if middle > list_of_integers[mid - 1] and middle > list_of_integers[mid + 1]:
        return peak
    elif middle < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
