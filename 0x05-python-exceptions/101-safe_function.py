#!/usr/bin/python3

import sys

def safe_function(fct, *args):
    try:
        div = fct(*args)
        return div
    except (ZeroDivisionError, IndexError) as msg:
        print("Exception: {}".format(msg), file=sys.stderr)
        return None
