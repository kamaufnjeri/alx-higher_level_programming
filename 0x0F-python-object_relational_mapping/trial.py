#!/usr/bin/python3
import sys

name = sys.argv[1]

if "fake" in name:
    print(name + "sucess")
else:
    print("failure")
