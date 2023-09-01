#!/usr/bin/python3
from urllib.request import urlopen
"""requesting a url"""


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    with urlopen(url) as body:
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body.read()}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
