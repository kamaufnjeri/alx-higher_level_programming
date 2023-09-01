#!/usr/bin/python3
"""request a url"""
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        value = {"email": sys.argv[2]}
        data = urlencode(value)
        data = data.encode('ascii')
        req = Request(url, data)
        with urlopen(req) as response:
            print(response.read())
    except IndexError:
        pass
