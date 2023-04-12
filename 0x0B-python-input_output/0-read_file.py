#!/usr/bin/python3
"""Reads into a text file"""


def read_file(filename=""):
    """open file using with"""

    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
