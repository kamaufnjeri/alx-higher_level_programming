#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        del a_dictionary[key]
        a_dictionary[key] = value
    return a_dictionary
