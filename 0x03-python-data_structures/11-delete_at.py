#!/usr/bin/python3


def delete_at(my_lists=[], idx=0):
    if idx < 0 or idx > (len(my_lists) - 1):
        return my_lists
    del my_lists[idx]
    return my_lists
