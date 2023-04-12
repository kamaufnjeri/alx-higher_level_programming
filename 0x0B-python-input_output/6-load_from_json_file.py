#!/usr/bin/python3
"""Reading from json file"""
import json


def load_from_json_file(filename):
    """python object to be created from  json file"""
    with open(filename, 'r', encoding='utf-8') as files:
        return(json.load(files))
