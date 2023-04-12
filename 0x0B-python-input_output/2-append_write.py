#!/usr/bin/python3
"""opens file appends to it and creates it if not existing"""


def append_write(filename="", text=""):
    """use with to open append a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        f.write(text)
        return len(text)
