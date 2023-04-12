#!/usr/bin/python3
"""decoding from JSON to python"""
import json

def from_json_string(my_str):
    """Returns json string decoded to python"""
    return json.loads(my_str)
