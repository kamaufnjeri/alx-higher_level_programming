#!/usr/bin/python3
"""save objects to json"""
import json


def save_to_json_file(my_obj, filename):
    """save opject to file"""
    with open(filename, 'w', encoding='utf-8') as files:
        json.dump(my_obj, files)
