#!/usr/bin/python3
""""Opens a file and writes into it and if not present creates it"""


def write_file(filename="", text=""):
    """use with to open file write and close it"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
        return len(text)
