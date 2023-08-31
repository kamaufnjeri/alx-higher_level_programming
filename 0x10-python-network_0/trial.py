#!/usr/binn/python3
"""Module to find a peak"""

def find_peak(list_of_integers):
    """The function"""
    lis = list_of_integers
    if len(lis) == 0:
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
        mid = (0 + len(lis) - 1) // 2

        for 
        l_peak = find_peak(lis[:mid])
        r_peak = find_peak(lis[mid:])

        if l_peak != None and r_peak != None:
            if l_peak >= r_peak and l_peak >= lis[mid]:
                return l_peak
            elif r_peak >= l_peak and r_peak >= lis[mid]:
                return r_peak
            else:
                return lis[mid]
