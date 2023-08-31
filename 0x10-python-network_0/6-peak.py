#!/usr/binn/python3
"""Module to find a peak"""

def find_peak(list_of_integers):
    """The function"""
    lis = list_of_integers
    if len(lis) == O:
        return None

    elif len(lis) == 1:
        return lis[0]

    elif len(lis) == 2:
        if lis[1] >= lis[0]:
            return lis[1]
        else:
            return lis[0]
    elif len(lis) == 3:
        if lis[1] >= lis[2] and lis[1] >= lis[0]:
            return lis[1]
    else:
        mid = 0 + len(lis) - 1 // 2
        
        if lis[mid] >= lis[mid - 1] and lis[mid] >= lis[mid - 1]:
            return lis[mid]
        else:
            l_peak = find_peak(lis[:mid])
            r_peak = find_peak(lis[mid:])

            if l_peak >= r_peak:
                return l_peak
            else:
                return r_peak
