#!/usr/bin/python3
import json
"""decoding from JSON to python"""


def from_json_string(my_str):
    """Returns json string decoded to python"""
    return json.loads(my_str)
